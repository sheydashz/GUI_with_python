import tkinter as tk


class ToolTip(object):
    def __init__(self,widget):
        self.widget=widget
        self.tipwindow=None
        self.id=None
        self.x=self.y=0

    def showtip(self,text):
        self.text=text
        if self.tipwindow or not  self.text:
            return
        x,y,_cx,_cy=self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + _cy +self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d'%(x,y))

        label= tk.Label(tw,text=self.text,justify=tk.LEFT,background="#fffe0",relief=tk.SOLID,
                        borderwidth=1,font=('tahoma','8','normal'))
        label.pack(id,padx=1)

    def hideTip(self):
        tw=self.tipwindow
        self.tipwindow=None
        if tw:
            tw.destroy()


def createToolTip(widget,text):
    toolTip=ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hideTip()
    widget.bind('<Enter>',enter)
    widget.bind('<Leave>',leave)
