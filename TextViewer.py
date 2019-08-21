import tkinter,os
from tkinter import ttk


class TreeWindows(tkinter.Frame):
    def __init__(self,master,path):
        frame=tkinter.Frame(master)
        frame.pack(side=tkinter.LEFT,fill=tkinter.Y)

        self.tree=ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)

        root=self.tree.insert("","end",text=os.path.basename(path),open=True,values=tuple(path.split('\\')))
        self.loadTree(root,path)
        self.sy=tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)

        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        self.InfoWindows=InfoWindows(win)
        self.tree.bind("<<TreeviewSelect>>",self.func)

    def func(self,event):
        v=event.widget.selection()
        for sv in v:
            file=self.tree.item(sv)["text"]
            self.InfoWindows.ev.set(file)
            absPath=self.tree.item(sv)['values']
            absPath='\\'.join(absPath)
            if os.path.splitext(absPath)[1] in ['.py','.md','.log','.ini','.pid']:
                text=open(absPath,'r')
                self.InfoWindows.text.delete(0.0, tkinter.END)
                self.InfoWindows.text.insert(tkinter.INSERT, text.read())
            else:
                self.InfoWindows.text.delete(0.0, tkinter.END)
            # if

    def loadTree(self,parent,path):
        dirNum=0
        for fileName in os.listdir(path):
            absPath=os.path.join(path,fileName)
            if os.path.isdir(absPath):
                treey = self.tree.insert(parent, dirNum, text=os.path.basename(absPath),values=tuple(absPath.split('\\')))
                dirNum+=1
                self.loadTree(treey,absPath)
            else:
                treey = self.tree.insert(parent, "end", text=os.path.basename(absPath),values=tuple(absPath.split('\\')))


class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.RIGHT,fill=tkinter.Y)

        self.ev=tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()

        self.text = tkinter.Text(frame)
        self.text.pack()

if __name__=="__main__":
    path=r"C:\Code\python\ABUS_presentation"
    win=tkinter.Tk()
    win.title("File Manager")
    win.geometry("600x400+200+50")
    TreeWindows(win,path)
    win.mainloop()