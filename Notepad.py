from tkinter import *
from tkinter import font
from tkinter.filedialog import *
import os
from tkinter.messagebox import *
import __main__ as main
import sys
#######################################################################################
notepad = Tk()
notepad.title('Notepad')
OS = sys.platform
File = main.__file__

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)

        def newfile():
            if OS.startswith('win'):
                os.popen('python %s' %File)
            if OS == 'linux':
                os.popen('python3 %s' %File)
            else:
                os.popen('python3 %s' %File)

        def newfile2(event):
            if OS.startswith('win'):
                os.popen('python %s' % File)
            if OS == 'linux':
                os.popen('python3 %s' % File)
            else:
                os.popen('python3 %s' % File)

        def savefile():
            file = asksaveasfile(title='Save File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            try:
                filename = str(file).split("'")[1]
                with open(filename, 'w') as file:
                    file.write(str(text_area.get(1.0, END)))
            except:
                pass

        def savefile2(event):
            file = asksaveasfile(title='Save File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            try:
                filename = str(file).split("'")[1]
                with open(filename, 'w') as file:
                    file.write(str(text_area.get(1.0, END)))
            except:
                pass

        def openfile():
            file = askopenfile(title='Open File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            try:
                filename = str(file).split("'")[1]
                with open(filename, 'r') as file:
                    data = file.read()
                    text_area.insert(INSERT, data)
                    notepad.title(filename)
            except:
                pass

        def openfile2(event):
            file = askopenfile(title='Open File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            try:
                filename = str(file).split("'")[1]
                with open(filename, 'r') as file:
                    data = file.read()
                    text_area.insert(INSERT, data)
                    notepad.title(filename)
            except:
                pass

        def selectAll(event):
            text_area.tag_add('sel', 1.0, END)

        def copy():
            try:
                text = text_area.selection_get()
                text_area.clipboard_clear()
                text_area.clipboard_append(text)
            except:
                pass

        def paste():
            try:
                text = text_area.clipboard_get()
                text_area.insert(INSERT, text)
            except:
                pass

        def cut():
            copy()
            try:
                text_area.delete('sel.first', 'sel.last')
            except:
                pass

        menu = Menu(self)

        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='New', command=newfile)
        filemenu.add_command(label='Save', command=savefile)
        filemenu.add_command(label='Open', command=openfile)
        filemenu.add_separator()
        filemenu.add_command(label='CLose')
        menu.add_cascade(label='File', menu=filemenu)
        notepad.config(menu=menu)

        editmenu = Menu(menu, tearoff=0)
        editmenu.add_command(label='Copy', command=copy)
        editmenu.add_command(label='Paste', command=paste)
        editmenu.add_command(label='Cut', command=cut)
        menu.add_cascade(label='Edit', menu=editmenu)

        scrollbary = Scrollbar(self)
        scrollbary.pack(side=RIGHT, fill='y')

        text_area = Text(self, bg="white", fg='black', yscrollcommand=scrollbary.set)
        text_area.pack(expand=YES, fill=BOTH)
        text_area['font'] = font.Font(size=15)
        notepad.bind('<Control-n>', newfile2)
        notepad.bind('<Control-s>', savefile2)
        notepad.bind('<Control-o>', openfile2)
        notepad.bind('<Control-a>', selectAll)

        def askClose():
            Q = askyesnocancel('Save', 'Do you want to save the file', icon='warning')
            if Q == 1:
                savefile()
            if Q == 0:
                notepad.quit()

        notepad.protocol('WM_DELETE_WINDOW', askClose)


app().mainloop()

