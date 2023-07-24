from tkinter import Tk
from .layout import Layout, LayoutArt


class Filter(Layout):
    def __init__(self) -> None:
        self.root = Tk()
        self.filtroWindow()
        self.frameFiltro()
        self.maindata()
        self.labelsFrame()
        self.entrysFrame()
        self.buttons()
        self.root.mainloop()

class ArtystemFilter(LayoutArt):
    def __init__(self) -> None:
        self.rootArtsystem = Tk()
        self.artsystemWindow()
        self.ArtsystemFrame()
        self.entrysFrameArtsystem()
        self.ArtsytemLabel()
        self.ArtsytemButtons()
        self.maindataArtsystenfiltro()
        self.rootArtsystem.mainloop()