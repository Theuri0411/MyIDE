from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
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
        path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    else:
        path = file_path
    with open(path, "W") as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == "":
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Please Save Code")
        text.pack()
        return
    command = f"python {file_path}"
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert("1.0", output)
    code_output.insert("1.0", error)


menubar = Menu(compiler)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save AS", command=save_as)
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file_menu)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label="Run", command=run)
menubar.add_cascade(label="Run", menu=runbar)

compiler.config(menu=menubar)
editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
