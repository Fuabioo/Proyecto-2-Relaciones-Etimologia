"""
Main Panel Module
"""

import tkinter


def fill_word_word(self):
    """Fills the widget with word-word query form"""
    tkinter.Label(self.frame, text="  Idiom #1").grid(row=1)
    tkinter.Entry(self.frame, name="idiom_1").grid(row=1, column=1)
    tkinter.Label(self.frame, text="  Word #1").grid(row=2)
    tkinter.Entry(self.frame, name="word_1").grid(row=2, column=1)
    tkinter.Label(self.frame, text="  Idiom #2").grid(row=3)
    tkinter.Entry(self.frame, name="idiom_2").grid(row=3, column=1)
    tkinter.Label(self.frame, text="  Word #2").grid(row=4)
    tkinter.Entry(self.frame, name="word_2").grid(row=4, column=1)
    self.items["brother_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Brothers?",
        onvalue=True,
        offvalue=False,
        variable=self.items["brother_bool"],
        indicatoron=0).grid(row=5, sticky="E" + "W")
    tkinter.Entry(self.frame, name="brother").grid(row=5, column=1)
    self.items["child_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Child?",
        onvalue=True,
        offvalue=False,
        variable=self.items["child_bool"],
        indicatoron=0).grid(row=6, sticky="E" + "W")
    tkinter.Entry(self.frame, name="child").grid(row=6, column=1)
    self.items["uncle_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Uncle?",
        onvalue=True,
        offvalue=False,
        variable=self.items["uncle_bool"],
        indicatoron=0).grid(row=7, sticky="E" + "W")
    tkinter.Entry(self.frame, name="uncle").grid(row=7, column=1)
    self.items["cousin_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Cousins?",
        onvalue=True,
        offvalue=False,
        variable=self.items["cousin_bool"],
        indicatoron=0).grid(row=8, sticky="E" + "W")
    tkinter.Entry(self.frame, name="cousin").grid(row=8, column=1)
    self.items["cousin_level_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Cousin_Level",
        onvalue=True,
        offvalue=False,
        variable=self.items["cousin_level_bool"],
        indicatoron=0).grid(row=9, sticky="E" + "W")
    tkinter.Entry(self.frame, name="cousin_level").grid(row=9, column=1)
    tkinter.Entry(
        self.frame,
        name="error",
        fg='red',
        bg='black',
        font="Consolas 8").grid(
            row=10,
            column=1,
            sticky="W" + "E")

    for widget in self.frame.winfo_children():
        if isinstance(widget, tkinter.Entry):
            entry_name = str(widget).split('.')[-1]
            if "word" not in entry_name and "idiom" not in entry_name:
                widget.bind("<Key>", lambda e: "break")


def fill_idiom_word(self):
    """Fills the widget with idiom-word query form"""
    tkinter.Label(self.frame, text="  Idiom").grid(row=1)
    tkinter.Entry(self.frame, name="idiom").grid(row=1, column=1)
    tkinter.Label(self.frame, text="  Word's Idiom").grid(row=2)
    tkinter.Entry(self.frame, name="word_idiom").grid(row=2, column=1)
    tkinter.Label(self.frame, text="  Word").grid(row=3)
    tkinter.Entry(self.frame, name="word").grid(row=3, column=1)
    self.items["related_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Related?",
        onvalue=True,
        offvalue=False,
        variable=self.items["related_bool"],
        indicatoron=0).grid(row=4, sticky="E" + "W")
    tkinter.Entry(self.frame, name="related").grid(row=4, column=1)
    self.items["originated_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Originated",
        onvalue=True,
        offvalue=False,
        variable=self.items["originated_bool"],
        indicatoron=0).grid(row=5, sticky="E" + "W")
    tkinter.Entry(self.frame, name="originated").grid(row=5, column=1)
    self.items["list_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  List related",
        onvalue=True,
        offvalue=False,
        variable=self.items["list_bool"],
        indicatoron=0).grid(row=6, sticky="E" + "W")
    tkinter.Entry(self.frame, name="listing").grid(row=6, column=1)
    tkinter.Entry(
        self.frame,
        name="error",
        fg='red',
        bg='black',
        font="Consolas 8").grid(
            row=7,
            column=1,
            sticky="W" + "E")

    for widget in self.frame.winfo_children():
        if isinstance(widget, tkinter.Entry):
            entry_name = str(widget).split('.')[-1]
            if "word" not in entry_name and "idiom" not in entry_name:
                widget.bind("<Key>", lambda e: "break")


def fill_idiom_idiom(self):
    """Fills the widget with idiom-idiom query form"""
    tkinter.Label(self.frame, text="  Idiom #1").grid(row=1)
    tkinter.Entry(self.frame, name="idiom_1").grid(row=1, column=1)
    tkinter.Label(self.frame, text="  Idiom #2").grid(row=2)
    tkinter.Entry(self.frame, name="idiom_2").grid(row=2, column=1)
    self.items["common_amount_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Common amount",
        onvalue=True,
        offvalue=False,
        variable=self.items["common_amount_bool"],
        indicatoron=0).grid(row=3, sticky="E" + "W")
    tkinter.Entry(self.frame, name="common_amount").grid(row=3, column=1)
    self.items["common_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Common words",
        onvalue=True,
        offvalue=False,
        variable=self.items["common_bool"],
        indicatoron=0).grid(row=4, sticky="E" + "W")
    tkinter.Entry(self.frame, name="common").grid(row=4, column=1)
    self.items["contributed_most_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Contributed most",
        onvalue=True,
        offvalue=False,
        variable=self.items["contributed_most_bool"],
        indicatoron=0).grid(row=5, sticky="E" + "W")
    tkinter.Entry(self.frame, name="contributed_most").grid(row=5, column=1)
    self.items["idiom_list_bool"] = tkinter.BooleanVar()
    tkinter.Checkbutton(
        self.frame,
        text="  Idiom list",
        onvalue=True,
        offvalue=False,
        variable=self.items["idiom_list_bool"],
        indicatoron=0).grid(row=6, sticky="E" + "W")
    tkinter.Entry(self.frame, name="idiom_list").grid(row=6, column=1)
    tkinter.Entry(
        self.frame,
        name="error",
        fg='red',
        bg='black',
        font="Consolas 8").grid(
            row=8,
            column=1,
            sticky="W" + "E")

    for widget in self.frame.winfo_children():
        if isinstance(widget, tkinter.Entry):
            entry_name = str(widget).split('.')[-1]
            if "idiom" not in entry_name or entry_name == "idiom_list":
                widget.bind("<Key>", lambda e: "break")
