#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
import webbrowser

class MainAppView(tk.Frame):

    def start_gui(self,start = True):

        if start:
            self.mainloop()
        else:
            self.master.destroy()

    def createWidgets(self):

        self.title = tk.Label(
                self, text = " Import your PDF of JPG file: ")
        self.title.grid(
            row=0, column=0,columnspan=1, sticky = tk.E+tk.W )

        self.one = tk.Button(self)
        self.one["text"] = "Import"
        self.one.grid(row=1, column=0)

        self.l1 = tk.Label(self)
        self.l1["text"] = "First Name"
        self.l1.grid(row=100, column=0, rowspan=1)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
