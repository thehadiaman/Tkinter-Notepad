from tkinter import *
from tkinter.filedialog import *
#######################################################################################
notepad = Tk()
notepad.title('Notepad')


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)

        def newfile():
            text_area.delete(1.0, END)

        def savefile():
            file = asksaveasfile(title='Save File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            filename = str(file).split("'")[1]

            try:
                with open(filename, 'w') as file:
                    file.write(str(text_area.get(1.0, END)))
            except:
                pass

        def openfile():
            file = askopenfile(title='Open File', filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            filename = str(file).split("'")[1]

            try:
                with open(filename, 'r') as file:
                    data = file.read()
                    text_area.insert(INSERT, data)
                    notepad.title(filename)
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
        editmenu.add_command(label='Copy')
        editmenu.add_command(label='Paste')
        editmenu.add_command(label='Cut')
        menu.add_cascade(label='Edit', menu=editmenu)

        scrollbary = Scrollbar(self)
        scrollbary.pack(side=RIGHT, fill='y')

        text_area = Text(self, bg="white", fg='black', yscrollcommand=scrollbary.set)
        text_area.pack(expand=YES, fill=BOTH)


app().mainloop()
