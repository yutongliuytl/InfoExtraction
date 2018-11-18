from MainAppView import MainAppView
import tkinter as tk
from tkinter import filedialog
import cv2

import OCR
import NLP

class MainAppController(object):

    def read(self):
        self.view.t1.delete(0,len(self.view.t1.get()))
        self.view.t2.delete(0,len(self.view.t2.get()))
        self.view.t3.delete(0,len(self.view.t3.get()))
        self.view.t4.delete(0,len(self.view.t4.get()))
        self.view.t5.delete(0,len(self.view.t5.get()))
        self.view.t6.delete(0,len(self.view.t6.get()))
        self.view.t7.delete(0,len(self.view.t7.get()))
        self.view.t8.delete(0,len(self.view.t8.get()))
        self.view.t9.delete(0,len(self.view.t9.get()))
        file_name = tk.filedialog.askopenfilename()
        OCR.OCR(file_name)
        data = NLP.NLP()
        self.view.t1.insert(0,data[3])
        self.view.t2.insert(0,data[4])
        self.view.t3.insert(0,data[0])
        self.view.t4.insert(0,data[5])
        self.view.t5.insert(0,data[7])
        self.view.t6.insert(0,data[1])
        self.view.t7.insert(0,data[2])
        self.view.t8.insert(0,data[6])
        self.view.t9.insert(0,data[8])
        

    def init_view(self,root):

        self.view = MainAppView(master=root)

        # Bind buttons with callback methods
        self.view.one["command"] = self.read

        # Start the gui
        self.view.start_gui()
