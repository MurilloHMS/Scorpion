from tkinter import Tk

from menu_package.menu import Menus
from conference_package.layout import Layout


class Conference(Layout, Menus):
    def __init__(self) -> None:
        self.root = Tk()
        self.mainWindow()
        self.windowframes()
        self.labelsMainWindow()
        self.entrysMainWindow()
        self.mainData()
        self.buttons()
        self.menu()
        self.root.mainloop()
