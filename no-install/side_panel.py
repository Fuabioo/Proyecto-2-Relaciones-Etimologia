import tkinter

class SidePanel():
    """Side panel with buttons"""
    """
    1. Rel:derived
    2. Rel:etymologically
    4. Rel:etymological_origin_of
    6. Rel:has_derived_form
    3. Rel:etymologically_related
    5. Rel:etymology
    7. Rel:is_derived_from
    8. Rel:variant:ortography
    """

    def __init__(self, root, populate):
        self.frame2 = tkinter.Frame(root, bg="black")
        self.frame2.grid(row=0, column=1)
        self.relations = {}
        def_font = "Consolas 8"
        tkinter.Label(
            self.frame2,
            text="\nSelect Relation(s)",
            font=def_font).pack(side="top", fill=tkinter.BOTH)

        self.relations["derived"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Derived",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["derived"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["etymologically"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Etymologically",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["etymologically"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["etymology"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Etymology",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["etymology"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["etymologically_related"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Etymology related",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["etymologically_related"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["has_derived_form"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Has derived form",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["has_derived_form"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["etymological_origin_of"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Etymological origin of",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["etymological_origin_of"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["is_derived_from"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Is derived from",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["is_derived_from"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)

        self.relations["variant"] = tkinter.BooleanVar()
        tkinter.Checkbutton(
            self.frame2,
            text="  Variant",
            font=def_font,
            onvalue=True,
            offvalue=False,
            variable=self.relations["variant"],
            indicatoron=0).pack(side="top", fill=tkinter.BOTH)


        tkinter.Label(
            self.frame2,
            text="\nSelect Query Form",
            font=def_font).pack(side="top", fill=tkinter.BOTH)
        self.word_word_butt = tkinter.Button(
            self.frame2,
            text="\"Word-Word\"",
            font=def_font,
            command=lambda: populate("word_word"))
        self.word_word_butt.pack(side="top", fill=tkinter.BOTH)
        self.idiom_word_butt = tkinter.Button(
            self.frame2,
            text="\"Idiom-Word\"",
            font=def_font,
            command=lambda: populate("idiom_word"))
        self.idiom_word_butt.pack(side="top", fill=tkinter.BOTH)
        self.idiom_idiom_butt = tkinter.Button(
            self.frame2,
            text="\"Idiom-Idiom\"",
            font=def_font,
            command=lambda: populate("idiom_idiom"))
        self.idiom_idiom_butt.pack(side="top", fill=tkinter.BOTH)
        self.separator = tkinter.Label(
            self.frame2,
            text=''.join(['_' * 30]),
            font=def_font)
        self.separator.pack(side="top", fill=tkinter.BOTH)
        self.search_btn = tkinter.Button(
            self.frame2,
            text="Search",
            font=def_font,
            bg="green")
        self.search_btn.pack(side="top", fill=tkinter.BOTH)
        self.clear_con_btn = tkinter.Button(
            self.frame2,
            text="Clear Console",
            font=def_font,
            bg="orange")
        self.clear_con_btn.pack(side="top", fill=tkinter.BOTH)
        self.clear_btn = tkinter.Button(
            self.frame2,
            text="Clear Form",
            font=def_font,
            bg="red")
        self.clear_btn.pack(side="top", fill=tkinter.BOTH)

    def set_separator(self, text):
        """Sets the displayed text on the separator.
        Given text must be: \"word_word\""""
        new_sep = "\n"
        new_sep += text.split("_")[0].upper()
        new_sep += " x "
        new_sep += text.split("_")[1].upper()
        self.separator.config(text=new_sep)


    def get_relations(self):
        """Gets the relations from the frame"""
        result = {}
        for relation, value in self.relations.items():
            try:
                value = value.get()
                result[relation] = value
            except BaseException:
                result[relation] = value
        return result