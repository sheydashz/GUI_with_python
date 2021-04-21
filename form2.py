import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class Form:
    def __init__(self,win):
        # Create Main Window
        self.mainWin=win
        self.colors = ['White', 'Gold', 'Blue', 'Green']


        self.mainFrame()
        self.nameQuantity()
        self.submitButton()
        self.checkButton()
        self.colorButtons()
        self.scrolledText()
        self.container()
        self.settings()

        # Display
        self.win.mainloop()

    def mainFrame(self):
        ## Create main LabelFrame
        self.win=tk.LabelFrame(self.mainWin,text='Entrance Form')
        self.win.grid(column=0,row=0)

    def nameQuantity(self):
        ##### Create Labels: Name and Quantity
        nameLable=tk.Label(self.win,text='Enter your name:')
        quanLable=tk.Label(self.win,text='Enter Quantity:')
        nameLable.grid(column=0,row=0,sticky=tk.W)
        quanLable.grid(column=1,row=0,sticky=tk.W)

        #### Create Name and Quantity Entries
        self.nameVar=tk.StringVar()
        self.quanVar=tk.StringVar()

        nameBox=ttk.Entry(self.win,textvariable=self.nameVar,width=12)
        nameBox.focus()
        nameBox.grid(column=0,row=1)
        quanBox=ttk.Combobox(self.win,textvariable=self.quanVar,width=12,state='readonly')
        quanBox['values']=(0,1,2,24,100)
        quanBox.current(0)
        quanBox.grid(column=1,row=1)

    def submitButton(self):
        self.enterButton = ttk.Button(self.win, text='Submit', command=self.submitFunc)
        self.enterButton.grid(column=3, row=1, sticky=tk.W)

    #### Create Enter Button: When clicked print Hello! "name"
    def submitFunc(self):
        if self.nameVar.get():
            self.enterButton.configure(text='Hello '+ self.nameVar.get()+'!!')
        else:
            self.enterButton.configure(text='Invalid Name Variable. Please Try again Later.')

    ### Create ChackButton
    def checkButton(self):
        check1=tk.Checkbutton(self.win,text='deactive',state='disabled')
        check2=tk.Checkbutton(self.win,text='activate')

        check1.select()
        check2.select()

        check1.grid(column=0,row=2,sticky=tk.W)
        check2.grid(column=1,row=2,sticky=tk.W)

    ### Create color Buttons
    def colorButtons(self):
        self.colorVar=tk.IntVar()
        for i in range(len(self.colors)):
            colorButton = tk.Radiobutton(self.win, text=self.colors[i], variable=self.colorVar, value=i, command=self.changeColor)
            colorButton.grid(column=i, row=3, sticky=tk.W)
    def changeColor(self):
        self.win.configure(background=self.colors[self.colorVar.get()])


    ### Create Scrolled text
    def scrolledText(self):
        scrollBox=scrolledtext.ScrolledText(self.win,width=30,height=3,wrap=tk.WORD)
        scrollBox.grid(column=0,columnspan=4)

    ### Create Container
    def container(self):
        container=ttk.LabelFrame(self.win,text='Labels: ')
        container.grid(column=1, row=7, padx=20, pady=40)
        ttk.Label(container,text='Label 1').grid(column=0,pady=4)
        ttk.Label(container,text='Label 2').grid(column=0,pady=4)

### Create Padding
    def settings(self):
        for child in self.win.winfo_children():
            child.grid_configure(padx=8,pady=4)

