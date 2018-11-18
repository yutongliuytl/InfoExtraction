from MainAppView import MainAppView
import tkinter as tk
from tkinter import filedialog
import cv2


class MainAppController(object):

    def read(self):
        file_name = tk.filedialog.askopenfilename()
        self.image = cv2.imread(file_name, 0)
        cv2.imshow("", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def init_view(self,root):

        self.view = MainAppView(master=root)

        # Bind buttons with callback methods
        self.view.one["command"] = self.read

        # Start the gui
        self.view.start_gui()
