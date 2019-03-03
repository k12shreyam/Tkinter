from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.geometry("1600x900") #x=1600 y=900
tk.title("GUI3")
tk['bg']="red"
obj_frame=Frame(tk,width=900,height=400)
obj_frame.place(x=200,y=200)
obj_label=Label(text="Student Detail\n Application",font=("arial",20,"bold")).place(x=600,y=50)
obj_label=Label(obj_frame,text="Name :",font=("arial",14,"underline")).place(x=100,y=50)
obj_entry=Entry(obj_frame).place(x=250,y=50)
obj_label=Label(obj_frame,text="Stream :",font=("arial",14,"underline")).place(x=100,y=100)
obj_entry=Entry(obj_frame).place(x=250,y=100)
obj_label=Label(obj_frame,text="Age :",font=("arial",14,"underline")).place(x=100,y=150)
obj_entry=Entry(obj_frame).place(x=250,y=150)
obj_label=Label(obj_frame,text="Contact no. :",font=("arial",14,"underline")).place(x=100,y=200)
obj_entry=Entry(obj_frame).place(x=250,y=200)

def btn():
    messagebox.showinfo(title="Login Status",message="Details saved successfully")

obj_btn=Button(obj_frame,text="Submit",font=("arial",14,"bold"),command=btn).place(x=450,y=300)
mainloop()
