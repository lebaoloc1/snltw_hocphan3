import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Initializing the file's pathname
file = None

#Creating the root window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("700x500")

#Creating the horizontal scrollbar
h_scroll = tk.Scrollbar(root, orient='horizontal')
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

#Creating the vertical scrollbar
v_scroll = tk.Scrollbar(root)
v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

#Creating the text area
text_area = tk.Text(root, font="lucida 13", wrap="none", xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
text_area.pack(expand=True, fill=tk.BOTH)

h_scroll.config(command=text_area.xview)
v_scroll.config(command=text_area.yview)

#Creating the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#Creating File menu and Edit menu
file_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu = tk.Menu(menu_bar, tearoff=0)

#Associating File menu and Edit menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

#Defining features for File menu's items and Edit menu's items
def newFile():
    global file
    file=None
    root.title("Untitled - Notepad")
    text_area.delete("1.0", tk.END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete("1.0", tk.END)
        f = open(file)
        text_area.insert("1.0", f.read())
        f.close()
    else:
        file = None


def saveFile():
    global file
    if file:
        f = open(file, "w")
        f.write(text_area.get("1.0", tk.END))
        f.close()
    else:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file:
            f = open(file, "w")
            f.write(text_area.get("1.0", tk.END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
        else:
            file = None


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def exitApplication():
    root.destroy()

#Adding new, open, save file and exit application features to the File menu
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitApplication)

#Adding cut, copy, paste features to the Edit menu
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

root.mainloop()
