import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root=tk.Tk()
root.title('11111')
root.geometry('500x300')
btn1=ttk.Button(root,text='click')
btn1.pack()
def test(e):
    messagebox.showinfo('ckmc','djcg')
btn1.bind('<Button-1>',test)
btn2=ttk.Button(root,text='21213')
btn2.pack()
btn2.bind('<Button-1>',test)
root.mainloop()
