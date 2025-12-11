import tkinter as tk
win = tk.Tk()
win.title('11111')
win.geometry('200x100')
var=tk.StringVar()
l = tk.Label(win,textvariable=var,
             bg='yellow',font=('Arial',12),width=15,height=2)
l.pack()
on_hit=False
win.mainloop()
def hit_me():
    global on_hit
    if on_hit == False:
        var.set('you fking hit me')
b=tk.BOTTOM(win,txt='hit me,b7',width=15,height=2,command=hit_me)