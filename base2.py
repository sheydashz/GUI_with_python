import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from form2 import Form

# Create Main Window
win=tk.Tk()
win.title('Python GUI')

# Create MenuBar
menubar=Menu(win)
win.configure(menu=menubar)

# Create file menu
def _quite():
    win.quit()
    win.destroy()
    exit()

fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=_quite)
menubar.add_cascade(label='File',menu=fileMenu)
aboutMenu=Menu(menubar,tearoff=0)
aboutMenu.add_command(label='help')
menubar.add_cascade(label='About',menu=aboutMenu)


# Create Bar
bar=ttk.Notebook(win)

# Create form tab
formTab=tk.Frame(bar)
bar.add(formTab,text='Form')

# Create Setting tab
settingTab=tk.Frame(bar)
bar.add(settingTab,text='Settings')

# Pack bar
bar.pack(expand=1,fill='both')

# add content to tab form
Form(formTab)

# Display
for child in menubar.winfo_children():
    child.grid_configure(pady=8,padx=8)
win.mainloop()