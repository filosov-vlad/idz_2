import inspect

lt = "abcdefg"
sg = "*+/-"
inp = "a\n"
char = ""
ind = -1

def read():
    global char, inp, ind
    #print(inp, inspect.stack()[1][3])
    char = inp[0]
    inp = inp[1:]
    ind += 1
    
def error():
    #print(inp)
    #print(char)
    raise AssertionError()

def cs():
    if char == "(" | "[":
        read()
        obsk()
        chsk()
            else:
                lt()
        if char == ")" | "]":
            read()
            if char == "\n":
                pass
            else:
                error()
        else:
            error()
    elif char in lt:
        read()
        if char == "\n":
            pass
        else:
            error()
    else:
        error()

def chsk():
    if char == "(":
        read()
        pbs()
        vir()
        vir_b()
        if char == ")":
            read()
        else:
            error()
        konec()
        
    elif char == "[":
        read()
        vir() -><-
        if char == "]":
            read()
        else:
            error()
        konec()
        
    elif char in lt:
        read()
        konec_np()
        
    else:
        error()


def obsk():
    if char == "[":
        read()
        vir()
        vir_b()
        else:
        pbs()
        vir()
        if char == "]":
            read()
        else:
            error()
        konec()
        
    elif char in lt:
        read()
        konec_bks_np()
        
    else:
        error()

def vir():
    if char == "(":
        read()
        op()
        else:
        op()
        vir_b()
        if char == ")":
            read()
        else:
            error()
        
    elif char == "[":
        read()
        vir()
        if char == "]":
            read()
        else:
            error()
            
    elif char in lt:
        read()
        
    else:
        error()

def pbs():
    if char == "[":
        read()
        lt()
         sq()
        if char == "]":
            read()
        else:
            error()
        
    elif char in lt:
        read()
        
    else:
        error()

def vir_b():
    if char == "[":
        read()
         sq()
        lt()
        if char == "]":
            read()
        else:
            error()
        
    elif char in lt:
        read()
        
    else:
        error()

def оп():
    if char in sg:
        read()
        lt()
         sq()
        lt()
    else:
        pass

def konec_np():
    if char in sg:
        read()
        vir_ok()
    else:
        error()

def konec_bks_np():
    if char in sg:
        read()
        vir_bks_ok()
    else:
        error()
    if char in lt:
        read(char)
    else:
        error()
    if char in sg:
        read(char)
    else:
        error()


    
if __name__ == "__main__":
    read()
    psz()


import tkinter as tk
from tkinter import messagebox

def confirm_text():
    global inp
    global ind
    ind = -1
    inp = text_field.get()+"\n"
    old_inp = inp
    if inp:
        try:
            read()
            psz()
            messagebox.showinfo("Done!", f"Your string is correct\nYou entered: {old_inp}")
        except:
            messagebox.showinfo("Error!", f"Something wrong with your string\nError symbol: \"{char}\"[{ind}]")
    else:
        messagebox.showerror("Error", "Please enter some text")

# create the main window
root = tk.Tk("DMiTI","DMiTI","DMiTI")
root.geometry("800x180")

# create the text field and button
input_label = tk.Label(root, text="Введите свою строку:")
text_field = tk.Entry(root)
confirm_button = tk.Button(root, text="Confirm", command=confirm_text)

# create the information box
info_label = tk.Label(root, text=
"""Правильная скобочная запись арифметических выражений с двумя видами скобок. 
Друг за другом на одном уровне вложенности могут стоять не более двух скобок. 
Каждая бинарная операция вместе с операндами берется в скобки. 
В правильной записи не могут присутствовать “лишние” (двойные) скобки и одна буква не может браться в скобки.

# pack the text field and button into the main window
input_label.pack()
text_field.pack(fill=tk.X, padx=5, pady=5) # fill horizontally, with 5 pixels of padding
confirm_button.pack(padx=5, pady=5)

info_label.pack()
# start the main loop
root.mainloop()
