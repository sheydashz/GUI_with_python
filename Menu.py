from tkinter import Menu


class MenuBar:
    def __init__(self,mainWindow,menuBar):
        self.fileMenu(menuBar)
        self.helpMenu(menuBar)
        self.win=mainWindow

    def fileMenu(self,menuBar):
        # create File Menu
        menuBar=menuBar
        file = Menu(menuBar, tearoff=0)
        file.add_command(label='New')
        file.add_separator()
        file.add_command(label='Exit',command=self._quit)
        menuBar.add_cascade(label='File', menu=file)

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def helpMenu(self,menuBar):
        # create Help Menu
        menuBar=menuBar
        help=Menu(menuBar,tearoff=0)
        help.add_command(label='Help')
        help.add_separator()
        help.add_command(label='Online')

        menuBar.add_cascade(label='Help',menu=help)