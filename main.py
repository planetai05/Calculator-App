# Creating a calculator using python
from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.configure(bg="grey")
global_list = []
def display0():
    listbox.insert(END,"0")
    global global_list
    global_list.append(0)
def display1():
    listbox.insert(END, "1")
    global global_list
    global_list.append(1)
def display2():
    listbox.insert(END,"2")
    global global_list
    global_list.append(2)
def display3(): 
    listbox.insert(END,"3")
    global global_list
    global_list.append(3)
def display4():
    listbox.insert(END,"4")
    global global_list
    global_list.append(4)
def display5():
    listbox.insert(END,'5')
    global global_list
    global_list.append(5)
def display6():
    listbox.insert(END,'6')
    global global_list
    global_list.append(6)
def display7():
    listbox.insert(END,'7')
    global global_list
    global_list.append(7)
def display8():
    listbox.insert(END,'8')
    global global_list
    global_list.append(8)
def display9():
    listbox.insert(END,'9')
    global global_list
    global_list.append(9)
def display_add():
    listbox.insert(END, "+")
    global global_list
    global_list.append("+")
def display_subtract():
    listbox.insert(END,"-")
    global global_list
    global_list.append("-")
def display_divide():
    listbox.insert(END,"÷")
    global global_list
    global_list.append("÷")
def display_multiply():
    listbox.insert(END,"x")
    global global_list
    global_list.append("x")
def display_result():
    listbox.insert(END,"=")
    global global_list
    if "+" in global_list:
        number = global_list.index("+")
        str1 = ""
        str2 = ""
        for val in range(number):
            str1 += str(global_list[val])
        for val in range(number+1, len(global_list)):
            str2 += str(global_list[val])
        listbox.insert(END, int(str1)+int(str2))
    if "-" in global_list:
        number = global_list.index("-")
        str1 = ""
        str2 = ""
        for val in range(number):
            str1 += str(global_list[val])
        for val in range(number+1, len(global_list)):
            str2 += str(global_list[val])
        listbox.insert(END, int(str1)-int(str2))
    if "x" in global_list:
        number = global_list.index("x")
        str1 = ""
        str2 = ""
        for val in range(number):
            str1 += str(global_list[val])
        for val in range(number+1, len(global_list)):
            str2 += str(global_list[val])
        listbox.insert(END, int(str1)*int(str2))
    if "÷" in global_list:
        number = global_list.index("÷")
        str1 = ""
        str2 = ""
        for val in range(number):
            str1 += str(global_list[val])
        for val in range(number+1, len(global_list)):
            str2 += str(global_list[val])
        listbox.insert(END, int(str1)/int(str2))


def display_clear():
    listbox.delete(0,END)
    global global_list
    global_list.clear()



button0 = Button(root, text="0", padx=25,pady=20, command=display0,bg="#616569",fg="white")
button1 = Button(root, text="1" ,padx=25,pady=20, command=display1,bg="#616569",fg="white")
button2 = Button(root, text="2", padx=25,pady=20, command=display2,bg="#616569",fg="white")
button3 = Button(root, text="3", padx=25,pady=20, command=display3,bg="#616569",fg="white")
button4 = Button(root, text="4", padx=25,pady=20, command=display4,bg="#616569",fg="white")
button5 = Button(root, text="5", padx=25,pady=20, command=display5,bg="#616569",fg="white")
button6 = Button(root, text="6", padx=25,pady=20, command=display6,bg="#616569",fg="white")
button7 = Button(root, text="7", padx=25,pady=20, command=display7,bg="#616569",fg="white")
button8 = Button(root, text="8", padx=25,pady=20, command=display8,bg="#616569",fg="white")
button9 = Button(root, text="9", padx=25,pady=20, command=display9,bg="#616569",fg="white")
button_add = Button(root, text="+", padx=25,pady=20, command=display_add, bg="#FFB20F",fg="white")
button_subtract = Button(root, text="-", padx=25,pady=20, command=display_subtract, bg="#FFB20F",fg="white")
button_divide = Button(root, text="÷", padx=25,pady=20, command=display_divide, bg="#FFB20F",fg="white")
button_multiply = Button(root, text="x", padx=25,pady=20, command=display_multiply, bg="#FFB20F",fg="white")
button_result = Button(root, text="=", padx=25,pady=20, command=display_result)
button_clear = Button(root, text='C', padx=25,pady=20, command=display_clear)
button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1) 
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_result.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
listbox = Entry(root, width=35, borderwidth=3, bg="black",fg="white")
listbox.grid(row=0,column=0, columnspan=4)


root=mainloop()
