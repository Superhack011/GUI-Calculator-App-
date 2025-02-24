from tkinter import *

def click(event):
    text= event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            value = eval(scvalue.get())

        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


x_root = Tk()

x_root.title('Calculator')
# x_root.wm_iconbitmap("2.ico")
# x_root.wm_iconbitmap("C:\Users\sande\OneDrive\Desktop\FOR_CCC\d42f8b8f1fef0dda7a891baff178c072.png")
x_root.geometry("425x540")

x_root.minsize(150,150)
x_root.maxsize(750,750)

scvalue = StringVar()
scvalue.set("")
screen = Entry(x_root, textvariable=scvalue,font="lucida 40 bold",background="lightyellow")
screen.pack(fill=X, padx=12, pady=12)

f1 = Frame(x_root, background="lightblue")
b = Button(f1,text="9",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="8",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="7",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="c",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack(padx=1, pady=1)

f1 = Frame(x_root, background="lightblue")
b = Button(f1,text="6",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="5",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="4",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="+",padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack(padx=1, pady=1)

f1 = Frame(x_root, background="lightblue")
b = Button(f1,text="3",padx=16, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="2",padx=16, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="1",padx=16, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="-",padx=16, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack(padx=1, pady=1)

f1 = Frame(x_root, background="lightblue")

b = Button(f1,text="0",padx=17, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="*",padx=17, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="/",padx=17, pady=10, font="lucida 25 bold")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="=",padx=15, pady=10, font="lucida 25 bold",background="blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack(padx=1, pady=1)


x_root.mainloop()