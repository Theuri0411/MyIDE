from tkinter import *

compiler = Tk()
compiler.title("MyIDE")


def run():
    print("Code will be run")


menubar = Menu(compiler)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label="Run", command=run)
menubar.add_cascade(label="Run", menu=runbar)
compiler.config(menu=menubar)
editor = Text()
editor.pack()
compiler.mainloop()
