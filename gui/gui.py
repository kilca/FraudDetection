import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from algo import *

class Toplevel1:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("628x450+423+154")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Amazon Fraud Detection")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.016, rely=0.044, relheight=0.456, relwidth=0.39)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.041, rely=0.0, height=21, width=64)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Values''')

        self.ListVals = tk.Listbox(self.Frame1, exportselection=0)
        self.ListVals.place(relx=0.082, rely=0.195, relheight=0.693
                , relwidth=0.751)
        self.ListVals.configure(background="white")
        self.ListVals.configure(disabledforeground="#a3a3a3")
        self.ListVals.configure(font="TkFixedFont")
        self.ListVals.configure(foreground="#000000")
        self.ListVals.insert("end","data/exampleIn.txt")

        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.43, rely=0.044, relheight=0.456, relwidth=0.47)

        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.ListAlgo = tk.Listbox(self.TFrame1, exportselection=0)
        self.ListAlgo.place(relx=0.102, rely=0.195, relheight=0.693
                , relwidth=0.793)
        self.ListAlgo.configure(background="white")
        self.ListAlgo.configure(disabledforeground="#a3a3a3")
        self.ListAlgo.configure(font="TkFixedFont")
        self.ListAlgo.configure(foreground="#000000")
        self.ListAlgo.insert("end","Fbox")
        self.ListAlgo.insert("end","Fraudar")
        self.ListAlgo.insert("end","Linear")

        self.Label2 = tk.Label(self.TFrame1)
        self.Label2.place(relx=0.102, rely=0.0, height=21, width=34)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Algo''')

        self.TFrame2 = ttk.Frame(self.top)
        self.TFrame2.place(relx=0.016, rely=0.533, relheight=0.389
                , relwidth=0.884)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")

        self.Label3 = tk.Label(self.TFrame2)
        self.Label3.place(relx=0.0, rely=0.0, height=21, width=44)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Output''')

        self.TextOutput = tk.Text(self.TFrame2)
        self.TextOutput.place(relx=0.018, rely=0.171, relheight=0.766
                , relwidth=0.962)
        self.TextOutput.configure(background="white")
        self.TextOutput.configure(font="TkTextFont")
        self.TextOutput.configure(foreground="black")
        self.TextOutput.configure(highlightbackground="#d9d9d9")
        self.TextOutput.configure(highlightcolor="black")
        self.TextOutput.configure(insertbackground="black")
        self.TextOutput.configure(selectbackground="blue")
        self.TextOutput.configure(selectforeground="white")
        self.TextOutput.configure(wrap="word")

        self.BtnExport = tk.Button(self.top)
        self.BtnExport.place(relx=0.908, rely=0.644, height=24, width=47)
        self.BtnExport.configure(activebackground="#ececec")
        self.BtnExport.configure(activeforeground="#000000")
        self.BtnExport.configure(background="#d9d9d9")
        self.BtnExport.configure(compound='left')
        self.BtnExport.configure(disabledforeground="#a3a3a3")
        self.BtnExport.configure(foreground="#000000")
        self.BtnExport.configure(highlightbackground="#d9d9d9")
        self.BtnExport.configure(highlightcolor="black")
        self.BtnExport.configure(pady="0")
        self.BtnExport.configure(text='''Export''')

        self.BtnEstimate = tk.Button(self.top, command=self.estimateClick)
        self.BtnEstimate.place(relx=0.908, rely=0.244, height=24, width=47)
        self.BtnEstimate.configure(activebackground="#ececec")
        self.BtnEstimate.configure(activeforeground="#000000")
        self.BtnEstimate.configure(background="#d9d9d9")
        self.BtnEstimate.configure(compound='left')
        self.BtnEstimate.configure(disabledforeground="#a3a3a3")
        self.BtnEstimate.configure(foreground="#000000")
        self.BtnEstimate.configure(highlightbackground="#d9d9d9")
        self.BtnEstimate.configure(highlightcolor="black")
        self.BtnEstimate.configure(pady="0")
        self.BtnEstimate.configure(text='''Estimate''')

    def estimateClick(self):
        print('click estimate')
        algo = ""
        for i in self.ListAlgo.curselection():
            algo = self.ListAlgo.get(i)
        data = ""
        for i in self.ListVals.curselection():
            data = self.ListVals.get(i)
        self.TextOutput.delete(1.0,END)#clear
        if (algo == "" or data == ""):
            self.TextOutput.insert(tk.END, "Please choose values and algo")
            return
        print('valid values')
        if (algo == "Fbox"):
            print('choose fbox')
            sus_users, sus_prod = runFbox(20,50,data)
            self.TextOutput.insert(tk.END,"suspicious users : "+str(len(sus_users))+"\n")
            self.insert(sus_users)
            self.TextOutput.insert(tk.END,"suspicious products : "+str(len(sus_prod))+"\n")
            self.insert(sus_prod)
        elif(algo == "Fraudar"):
            output = runFraudar(data)
            for o in output:
                self.TextOutput.insert(tk.END,str(o)+"\n")
        elif(algo == "Linear"):
            output = runLinear(data)
            for o in output:
                self.TextOutput.insert(tk.END,str(o)+"\n")

    def insert(self, vals):
        for v in vals:
            self.TextOutput.insert(tk.END,str(v)+"\n")
        

def start_up():
    root = tk.Tk()
    tl = Toplevel1(root)
    root.mainloop()


if __name__ == '__main__':
   start_up()
