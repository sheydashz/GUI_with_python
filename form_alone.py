import tkinter as tk
from tkinter import ttk,Menu,messagebox as mBox
from tkinter import scrolledtext
import time

# Create Main Window
mainWin=tk.Tk()
mainWin.title('Python GUI')
mainWin.iconbitmap('logo.jpg')

menuBar=Menu(mainWin)
mainWin.configure(menu=menuBar)
# Create File Menu
fileBar=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='File',menu=fileBar)
fileBar.add_command(label='New')
fileBar.add_separator()
fileBar.add_command(label='Exit')

#Create About Menu
def _msgBox():
    mBox.showinfo('GUI programming in python','This is a tutorial on GUI programming in python.')
aboutBar=Menu(menuBar)
menuBar.add_cascade(label='About',menu=aboutBar)
aboutBar.add_command(label='Info',command=_msgBox)

# menuBar.pack(expand=1,fill='both')

## Create main LabelFrame
win=tk.LabelFrame(mainWin,text='Entrance Form')
win.grid(column=0,row=0)

##### Create Labels: Name and Quantity
nameLable=tk.Label(win,text='Enter your name:')
quanLable=tk.Label(win,text='Enter Quantity:')
nameLable.grid(column=0,row=0,sticky=tk.W)
quanLable.grid(column=1,row=0,sticky=tk.W)

#### Create Name and Quantity Entries
nameVar=tk.StringVar()
quanVar=tk.StringVar()

def checkStatus(*args,**kwargs):
    if not nameVar.get():
        mBox.showwarning('warning!','Please fill name field first.')
    elif nameVar.get()=='sheyda' and int(quanVar.get())<20:
        mBox.showwarning('ERROR','Your quantity must be higher than 20')
    else:
        pass
nameBox=ttk.Entry(win,textvariable=nameVar,width=12)
nameBox.focus()
nameBox.grid(column=0,row=1)
quanBox=ttk.Combobox(win,textvariable=quanVar,width=12,state='readonly')
quanBox.bind("<<ComboboxSelected>>", checkStatus)
quanBox['values']=(0,1,2,24,100)
quanBox.current(0)
quanBox.grid(column=1,row=1)

#### Create Enter Button: When clicked print Hello! "name"
def submitFunc():
    if nameVar.get():
        enterButton.configure(text='Hello '+ nameVar.get()+'!!')
    else:
        enterButton.configure(text='Invalid Name Variable. Please Try again Later.')


enterButton=ttk.Button(win,text='Submit',command=submitFunc)
enterButton.grid(column=3,row=1,sticky=tk.W)

### Create ChackButton

def checked():
    if check2Var.get()==1:
        answer=mBox.askyesno("choose",'Are you sure you want to activate this feature?')
        if answer == False:
            check2.deselect()
    else:
        pass

check2Var=tk.BooleanVar()
check1=tk.Checkbutton(win,text='deactive',state='disabled')
check2=tk.Checkbutton(win,text='activate',command=checked,variable=check2Var)

check1.select()

check1.grid(column=0,row=2,sticky=tk.W)
check2.grid(column=1,row=2,sticky=tk.W)

### Create color Buttons
colors=['White','Gold','Blue','Green']
colorVar=tk.IntVar()
def changeColor():
    win.configure(background=colors[colorVar.get()])

for i in range(len(colors)):
    colorButton=tk.Radiobutton(win,text=colors[i],variable=colorVar,value=i,command=changeColor)
    colorButton.grid(column=i,row=3,sticky=tk.W)

### Create Scrolled text
scrollBox=scrolledtext.ScrolledText(win,width=30,height=8,wrap=tk.WORD)
scrollBox.grid(column=0,columnspan=4)

## Create Spinbox
def printSpin():
    scrollBox.delete(1.0,tk.END)
    for i in range(int(spin.get())):
        scrollBox.insert(tk.INSERT,'%d. Hello!!\n'%i)
spin=tk.Spinbox(win,from_=0,to=10,bd=17,command=printSpin)
spin.grid(column=0,row=6)
spin2=tk.Spinbox(win,values=(1,2,5,24,100),relief=tk.SUNKEN)
spin2.grid(column=3,row=6)

### Create Container
container=ttk.LabelFrame(win,text='Labels: ')
container.grid(column=1, row=7, padx=20, pady=40)
ttk.Label(container,text='Label 1').grid(column=0,pady=4)
ttk.Label(container,text='Label 2').grid(column=0,pady=4)

### Create Padding
for child in win.winfo_children():
    child.grid_configure(padx=8,pady=4)

for child in win.winfo_children():
    child.grid_configure(padx=8,pady=4)
# Display
win.mainloop()
