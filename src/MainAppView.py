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
        self.one["text"] = "Populate"
        self.one.grid(row=1, column=0)

        self.l1 = tk.Label(self)

        self.l1["text"] = "First Name"
        self.l1.grid(row=2, column=0)

        self.t1 = tk.Entry(self)
        self.t1.grid(row=2, column=1)

        self.l2 = tk.Label(self)
        self.l2["text"] = "Last Name"
        self.l2.grid(row=3, column=0)

        self.t2 = tk.Entry(self)
        self.t2.grid(row=3, column=1)

        self.l3 = tk.Label(self)
        self.l3["text"] = "Date of Birth"
        self.l3.grid(row=4, column=0)

        self.t3 = tk.Entry(self)
        self.t3.grid(row=4, column=1)

        self.l4 = tk.Label(self)
        self.l4["text"] = "Nationality"
        self.l4.grid(row=5, column=0)

        self.t4 = tk.Entry(self)
        self.t4.grid(row=5, column=1)

        self.l5 = tk.Label(self)
        self.l5["text"] = "Height"
        self.l5.grid(row=6, column=0)

        self.t5 = tk.Entry(self)
        self.t5.grid(row=6, column=1)

        self.l6 = tk.Label(self)
        self.l6["text"] = "Country of Origin"
        self.l6.grid(row=7, column=0)

        self.t6 = tk.Entry(self)
        self.t6.grid(row=7, column=1)

        self.l7 = tk.Label(self)
        self.l7["text"] = "Mother Tongue"
        self.l7.grid(row=8, column=0)

        self.t7 = tk.Entry(self)
        self.t7.grid(row=8, column=1)

        self.l8 = tk.Label(self)
        self.l8["text"] = "Weight"
        self.l8.grid(row=9, column=0)

        self.t8 = tk.Entry(self)
        self.t8.grid(row=9, column=1)

        self.l9 = tk.Label(self)
        self.l9["text"] = "Income"
        self.l9.grid(row=10, column=0)

        self.t9 = tk.Entry(self)
        self.t9.grid(row=10, column=1)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
