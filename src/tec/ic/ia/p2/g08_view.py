"""
View Component of the application
"""

import logging
import types
import tkinter

from .g08_main_panel import fill_word_word, fill_idiom_word, fill_idiom_idiom
from .g08_side_panel import SidePanel


class View(object):
    """View class"""

    def __init__(self, root, debug=False, scaling=2.0):
        self.debug = debug
        self.root = root
        self.current_action = "word_word"
        self.scaling = scaling
        self.root.tk.call('tk', 'scaling', self.scaling)
        self.root.tk.call('encoding', 'system', 'utf-8')
        self.main_panel = None
        self.create_base()

    def load_data(self):
        """Loads the necessary data for the GUI"""
        if self.debug:
            print("Loading data")

    def create_base(self):
        """Creates the base for the root window"""
        if self.debug:
            print("Creating base")
        self.console_panel = ConsolePanel(self.root)
        self.side_panel = SidePanel(self.root, self.populate_main_panel)
        self.side_panel.set_separator("word_word")
        self.main_panel = MainPanel(self.root, action="word_word")

    def populate_main_panel(self, action: str):
        """Populates the main panel depending on the desired option"""
        self.main_panel.destroy()

        actions = dict(
            word_word=fill_word_word,
            idiom_word=fill_idiom_word,
            idiom_idiom=fill_idiom_idiom)

        self.main_panel = MainPanel(self.root, action, actions[action])
        self.side_panel.set_separator(action)
        self.current_action = action


class MainPanel():
    """Main panel"""

    def __init__(self, root, action="", func=None):
        self.action = action
        self.frame = tkinter.Frame(root, name=action)
        self.frame.grid(row=0, column=2)
        self.items = {}
        if func is not None:
            self.fill_panel = types.MethodType(func, self)
        self.fill_panel()

    def fill_panel(self):
        """Fills the panel"""
        text = "                    Select a query form"
        tkinter.Label(self.frame, text=text).grid(row=1)

    def get_inputs(self):
        """Gets the inputs from the frame"""
        for widget in self.frame.winfo_children():
            if isinstance(widget, tkinter.Entry):
                entry_name = str(widget).split('.')[-1]
                entry_value = widget.get()
                self.items[entry_name] = entry_value
        return self.items

    def set_inputs(self, inputs: dict):
        """Sets the values displayed on the frame"""
        for name in inputs:
            try:
                self.frame.nametowidget(name).delete(0, tkinter.END)
                self.frame.nametowidget(name).insert(0, inputs[name])
            except BaseException:
                continue

    def reset_inputs(self):
        """Sets the values displayed on the frame"""
        for widget in self.frame.winfo_children():
            if isinstance(widget, tkinter.Entry):
                widget.delete(0, tkinter.END)
                widget.insert(0, "")
            elif isinstance(widget, tkinter.Checkbutton):
                widget.deselect()

    def destroy(self):
        """Destroys the frame"""
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        self.items = {}


class TextHandler(logging.Handler):
    """This class allows you to log to tkinter"""

    def __init__(self, console):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.console = console

    def emit(self, record):
        """Emits a messege to the console"""
        msg = self.format(record)
        self.console.print(msg)


class ConsolePanel():
    """Side panel with a console output"""

    def __init__(self, root):
        self.console = tkinter.Frame(root)
        self.console.grid(row=0, column=0, sticky="N" + "S" + "E" + "W")

        tkinter.Text(
            self.console,
            bg="black",
            fg="white",
            width=75,
            height=42,
            font="Consolas 6",
            name="console").pack()
        self.console.nametowidget("console").insert(
            tkinter.INSERT, "Output Log Console\n")

    def print(self, *args):
        """
        Prints in the console
        """
        string = ""
        for arg in args:
            string += str(arg) + ' '
        string = string[:-1] + '\n'
        # string = bytes(string, 'utf-8').decode('utf-8', 'ignore')
        # string=string.decode('utf-8','ignore').encode("utf-8")
        # string = string.rstrip().encode('utf-8','ignore')
        char_list = [string[j] for j in range(len(string)) if ord(string[j]) in range(65536)]
        string=''
        for j in char_list:
            string=string+j
        self.console.nametowidget("console").insert(tkinter.END, string)
        self.console.nametowidget("console").see(tkinter.END)
        return True

    def clear(self):
        self.console.nametowidget("console").delete('1.0', tkinter.END)
