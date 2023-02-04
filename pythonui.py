import tkinter.simpledialog
import tkinter.messagebox
from tkinter import filedialog as fd

import os

# Dialog Boxes
def PasswordInputBox(title, content):
    char = "*"
    tkinter.Tk().withdraw()
    return tkinter.simpledialog.askstring(title, content, show=char)

def TextInputBox(title, content, char):
    tkinter.Tk().withdraw()
    return tkinter.simpledialog.askstring(title, content)

# GUI Output
def MessageBox(title, content):
    tkinter.messagebox.showinfo(title, content)
def WarningBox(title, content):
    tkinter.messagebox.showwarning(title, content)
def ErrorBox(title, content):
    tkinter.messagebox.showerror(title, content)

# Question Boxes
def AskQuestionBox(title, content):
    return tkinter.messagebox.askquestion(title, content)
def AskOkCancelBox(title, content):
    return tkinter.messagebox.askokcancel(title, content)
def AskRetry(title, content):
    return tkinter.messagebox.askretrycancel(title, content)

# Yes No Boxes
def AskYesNoBox(title, content):
    return tkinter.messagebox.askyesno(title, content)
def AskYesNoCancelBox(title, content):
    return tkinter.messagebox.askyesnocancel(title, content)


# File Manager
def FileWindow(defaultExtension):
    filetypes = (
        ('text files', '*'+defaultExtension),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    return filename

def FilesWindow(defaultExtension):
    filetypes = (
        ('text files', '*'+defaultExtension),
        ('All files', '*.*')
    )
    filenames = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filenames
    )
    return filenames

def FolderWindow():
    tk = tkinter.Tk()
    tk.withdraw()
    return fd.askdirectory()

# Command
def ExecuteSudoCommand(password, command):
    os.system("echo "+password+" | sudo -S "+command)
def ExecuteCommand(command):
    os.system(command)