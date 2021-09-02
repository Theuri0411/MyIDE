from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
compiler = Tk()
compiler.title("My_IDE")
file_path = ""


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[("python Files", "*.py")])
    with open(path, "r") as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        set_file_path(path)


def save_as():
    if file_path == "":
        path = asksaveasfilename(filetypes=[("python Files", "*.py")])
    else:
        path = file_path
    with open(path, "W") as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)


def run():
    code = editor.get("1.0", END)
    exec(code)


menubar = Menu(compiler)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=run)
file_menu.add_command(label="Save AS", command=save_as)
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file_menu)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label="Run", command=run)
menubar.add_cascade(label="Run", menu=runbar)

compiler.config(menu=menubar)
editor = Text()
editor.pack()
compiler.mainloop()
