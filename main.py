from tkinter import *
from tkinter.filedialog import asksaveasfilename


def run():
    code = editor.get("1.0", END)
    exec(code)


menubar = Menu(compiler)


def save_as():


file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=run)
file_menu.add_command(label="Save", command=run)
file_menu.add_command(label="Save AS", command=run)
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file_menu)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label="Run", command=run)
menubar.add_cascade(label="Run", menu=runbar)

compiler.config(menu=menubar)
editor = Text()
editor.pack()
compiler.mainloop()
