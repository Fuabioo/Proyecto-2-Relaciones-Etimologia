"""
Model Module
"""
import os
import time

from pyDatalog import pyDatalog


def get_files(filename):
    """Obtains all related files"""
    result = []
    file_exists = False
    criteria = filename.replace('*', '')
    for file in os.listdir(os.getcwd() + "\\database\\"):
        if criteria in file:
            result.append(file)
            file_exists = True
    return result, file_exists


class Model(pyDatalog.Mixin):
    """Model class, this handles any data related operation"""

    def __init__(self, filename="cl", debug=False):
        self.debug = debug
        self.clfile = self.set_cl_file(filename)
        self.data = ""
        self.use = False
        self.included_files = ""

    def load(self, console):
        """Loads the clauses from the file"""
        start = time.time()
        try:
            pyDatalog.load(self.data)
            if console:
                console.print(self.included_files,
                              "Finished ", time.time() - start, " s")
        except BaseException as exception:
            print(exception)

    def append_data(self, data, file=""):
        """Appends clauses to the current clause
        data can be a list of strings or a string"""
        if file:
            self.included_files += '> ' + file.split('\\')[-1] + '\n'
        if isinstance(data, str):
            self.data += data + '\n'
        elif isinstance(data, list):
            for meta in data:
                self.data += meta + '\n'

    def clear(self):
        """Clears the current data"""
        pyDatalog.Logic()  # Initializes Logic context for this thread
        self.included_files = ""
        self.data = ""

    def set_cl_file(self, filename):
        """Setter of cl file"""
        if ".cl" not in filename:
            filename += ".cl"
        self.clfile = os.getcwd() + "\\database\\" + filename

    def parse_file(self, cl_file=""):
        """Parses the file"""

        # pyDatalog.Logic()  # Initializes Logic context for this thread
        # start = time.time()

        if not cl_file:
            cl_file = self.clfile

        result = os.path.isfile(cl_file)
        if result:

            with open(cl_file, 'r', encoding="utf-8") as knowledge_base:
                # pyDatalog.load(knowledge_base.read())
                # knowledge_base.close()
                self.data = knowledge_base.read()

            # console.print(cl_file.split('\\')[-1],
            #               "Finished ", time.time() - start, " s")
            # self.data = pyDatalog.Logic(True)

        return result

    def get_logic(self):
        """Getter for the pyDatalog Logic"""
        if self.debug:
            print("Getting logic")
        return pyDatalog.Logic(True)

    def __str__(self):
        string = ""
        string += "---- File ----\n"
        string += self.clfile + '\n'
        string += "---- Data ----\n"
        string += self.data
        return string
