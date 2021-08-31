from tkinter import *

compiler = Tk()
compiler.title("MyIDE")

menubar = Menu(compiler)

runbar = Menu(menubar)
runbar.add_command(label="Run")
menubar.add_cascade(label = "Run", menu=runbar)
compiler.config(menu=menubar)

editor = Text()
editor.pack()
compiler.mainloop()
