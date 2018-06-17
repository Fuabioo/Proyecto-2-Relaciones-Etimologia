"""
Controller Module
"""

import tkinter
import logging
import threading
from copy import deepcopy

from .g08_view import View, TextHandler
from .g08_model import Model, get_files
from .g08_query import word_word, idiom_word, idiom_idiom


class Controller(object):
    """Controller class, it understands both the view and the controller"""

    def __init__(self, debug=False):
        self.debug = debug
        self.root = tkinter.Tk()
        self.view = View(self.root, debug)
        self.view.side_panel.search_btn.bind("<Button>", self.search)
        self.view.side_panel.clear_btn.bind("<Button>", self.clear)
        self.view.side_panel.clear_con_btn.bind("<Button>", self.clear_console)
        self.querys = dict(
            word_word=word_word,
            idiom_word=idiom_word,
            idiom_idiom=idiom_idiom)
        self.logics = {}
        self.busy = False
        self.model = Model()

        console_handler = TextHandler(self.view.console_panel)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.logger.addHandler(console_handler)

    def get_model(self, inputs, relations, work_relations):
        """Obtains the logic data from each relation's data,
        then executes the query and displays the results"""
        self.view.console_panel.print("Getting model")
        self.busy = True
        # Clear current model
        self.model.clear()
        # Initialize data pool
        data = []
        # Fill pool from data in submodels
        for thread in self.logics:
            is_the_relation = thread[4:-7] in work_relations
            if is_the_relation and self.logics[thread].use:
                data.append(self.logics[thread].data)
                self.model.append_data(
                    self.logics[thread].data,
                    self.logics[thread].clfile)
                self.logics[thread].use = False

        # Load data in model
        self.model.load(self.view.console_panel)

        self.view.console_panel.print(
            "Loaded", len(data), "logic models")
        # Execute query
        try:
            outputs = self.querys[self.view.current_action](
                deepcopy(inputs),
                deepcopy(relations),
                self.view.console_panel,
                self.model.get_logic())
        except BaseException as exeption:
            outputs = {"error": "Unable to process"}
            self.view.console_panel.print(exeption)
        # Display outputs
        self.view.main_panel.set_inputs(outputs)
        self.view.console_panel.print("Done.")
        self.busy = False

    def build_threads_aux(self, idiom_1, idiom_2, relations):
        """Obtains all threads for the given idiom order - relation"""
        results = []
        for relation, value in relations.items():
            if value:
                string = idiom_1 + '_'
                string += relation + '_'
                string += idiom_2
                # Check multiplicity
                files, exists = get_files(string)
                if exists:
                    results = results + files
                if not exists:
                    self.view.console_panel.print(
                        string + ".cl", "does not exist")
                    # Prevent predicate doesn't exist error
                    relations[relation] = False
        return results

    def build_threads(self, inputs, relations):
        """Builds the thread names for the given inputs"""
        idioms = []
        results = []

        # Obtain if it needs to be bidirectional
        bidirectional = False
        if "related_bool" in inputs and inputs["related_bool"]:
            bidirectional = True
        if "originated_bool" in inputs and inputs["originated_bool"]:
            bidirectional = True
        if "common_amount_bool" in inputs and inputs["common_amount_bool"]:
            bidirectional = True
        if "common_bool" in inputs and inputs["common_bool"]:
            bidirectional = True
        if "contributed_most_bool" in inputs and inputs["contributed_most_bool"]:
            bidirectional = True
        if "idiom_list_bool" in inputs and inputs["idiom_list_bool"]:
            bidirectional = True

        for key in inputs:
            if "idiom" in key and inputs[key]:  # and "word" not in key
                idioms.append(inputs[key])

        idiom_1 = '*'
        idiom_2 = '*'
        idiom_amount = len(idioms)
        if idiom_amount == 1:
            idiom_1 = idioms[0]
        if idiom_amount == 2:
            idiom_1 = idioms[0]
            idiom_2 = idioms[1]
        if "list_bool" in inputs and inputs["list_bool"]:
            idiom_2 = idioms[1]
            idiom_1 = '*'
            bidirectional = True
        if "contributed_most_bool" in inputs and inputs["contributed_most_bool"]:
            idiom_2 = idioms[0]
            idiom_1 = '*'
            bidirectional = True

        results = self.build_threads_aux(idiom_1, idiom_2, deepcopy(relations))
        if bidirectional:
            inverted = self.build_threads_aux(
                idiom_2, idiom_1, deepcopy(relations))
            results = results + inverted

        if self.debug:
            self.view.console_panel.print("THREAD", results)
        return results

    def get_thread(self, inputs, relations):
        """Obtains and runs all necessary threads.necessary
        PyDatalog manages logics per thread, so this way we retain
        a separate knowledge base in each thread and use only the
        necessary relations for each specific query
        * This requires that each thread has its own model"""
        threads = []
        result = True
        try:
            threads = self.build_threads(inputs, relations)
        except BaseException:
            self.view.console_panel.print("Unable to get inputs")
            result = False
        for thread in threads:
            if thread not in self.logics:
                self.logics[thread] = Model()
                self.logics[thread].set_cl_file(thread)
                self.logics[thread].parse_file()
            self.logics[thread].use = True
        if self.debug:
            self.view.console_panel.print(self.logics)
        return result

    def run(self):
        """Runs the controller itself"""
        self.root.title("Etymology relations")
        self.root.geometry("1080x600")
        self.root.deiconify()
        self.root.mainloop()

    def get_inputs(self):
        """Preprocesses the data for query"""
        inputs = self.view.main_panel.get_inputs()
        result = {}
        for _input in inputs:
            value = inputs[_input]
            if "bool" in _input and not isinstance(value, bool):
                value = value.get()
            result[_input] = value
        return result

    def clear(self, event):
        """Clears all the fields of the form"""
        if self.debug:
            print("Clearing...", str(event), event)
        self.view.main_panel.reset_inputs()

    def clear_console(self, event):
        """Clears the console panel text"""
        if self.debug:
            print("Clearing...", str(event), event)
        self.view.console_panel.clear()

    def check_relations(self, relations):
        """Checks if the relations are correct"""
        if self.debug:
            print("Checking relations")
        result = False
        work_relations = []

        # Eliminate unnecessary(duplicated) clauses
        if relations["is_derived_from"]:
            relations["has_derived_form"] = True
            relations["is_derived_from"] = False
        if relations["etymology"]:
            relations["etymological_origin_of"] = True
            relations["etymology"] = False

        for relation in relations:
            if relations[relation]:
                result = True
                work_relations.append(relation)
        return result, work_relations

    def check_inputs(self, inputs):
        """Checks if the inputs are correct"""
        if self.debug:
            print("Checking inputs")
        result = True
        for _input in inputs:
            if "word_" in _input and inputs[_input] == "":
                result = False
            elif "idiom_" in _input and inputs[_input] == "":
                if "list" not in _input:
                    result = False
        return result

    def search(self, event):
        """Processes the query event
        Requests a preprocessing of the inputs
        Obtains the outputs from the query module
        Requests the setting for the outputs on the gui"""
        if self.debug:
            print("Searching...", str(event), event)
        self.view.main_panel.set_inputs({"error": ""})
        inputs = self.get_inputs()
        relations = self.view.side_panel.get_relations()
        inputs_ok = self.check_inputs(inputs)
        relations_ok, work_relations = self.check_relations(relations)
        # deepcopy(relations))
        if inputs_ok and relations_ok:
            loaded_threads = self.get_thread(inputs, relations)
            if self.busy and loaded_threads:
                self.view.main_panel.set_inputs({"error": "Busy, please wait"})
            else:
                thread = threading.Thread(
                    name="model_getter",
                    target=self.get_model,
                    args=(inputs, relations, work_relations,))
                thread.start()
        else:
            error_str = ""
            if not relations_ok:
                error_str = "Select relation "
            elif not inputs_ok:
                error_str = "Fill inputs "
            self.view.main_panel.set_inputs({"error": error_str})
