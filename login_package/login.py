# Modulos Python
from tkinter import Tk

# Modulos do programa
from login_package.layout import Layout


class Login(Layout):
    def __init__(self) -> None:
        self.root = Tk()
        self.window()
        self.frames()
        self.image()
        self.Labels()
        self.entrys()
        self.buttons()
        self.root.mainloop()


