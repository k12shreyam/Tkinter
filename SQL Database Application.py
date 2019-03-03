from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("1080x600")
obj.title("GUI1")
obj['bg']="grey"
#frames on tkinter object obj
obj_frame=Frame(obj,width=900,height=400)
obj_frame.place(x=100,y=100)
#label on frames obj_Frame to print some message 
obj_label=Label(obj_frame,text="SQL DATABASE APPLICATION",font=("arial",20,"bold"))
obj_label.place(x=250,y=50)
obj_label_pfname=Label(obj_frame,text="File Name : ").place(x=50,y=100)
obj_label_gfname=Entry(obj_frame).place(x=120,y=100)
def connect():
    messagebox.showinfo(title="Connection status",message="Congratulations!!! \n \
    You are now connected to the database")
obj_btn=Button(obj_frame,text="Connect",font=("arial",10,"bold"),command=connect)
obj_btn.place(x=100,y=150)
obj.mainloop()
