import tkinter as tk
from tkinter import *

from MainAppController import MainAppController

def main():

    controller = MainAppController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Info Extraction')
    root.geometry('600x400')

    controller.init_view(root)


if __name__ == "__main__":
    main()
