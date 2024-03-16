# from tkinter import *

# root = Tk()
# root.mainloop()



# from tkinter import *

# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")

# # placing Entry widget to our GUI app
# entry = Entry(root, bg="yellow", fg="red", bd=5)
# entry.place(x=100,y=100)

# root.geometry('250x200')
# root.mainloop()



from tkinter import *

# creating root window
root = Tk()
root.title("Welcome to Instagram")
def login():
    print("Successfully Logined")
lbl1=Label(root,text="Login to Instagram")
lbl1.pack()
lbl2=Label(root,text="Username")


lbl2.pack()
# placing Entry widget to our GUI app
entry1 = Entry(root, bg="white", fg="blue", bd=2)
entry1.pack()
lbl3=Label(root,text="Password")
lbl3.pack()
entry2 = Entry(root, bg="white", fg="blue", bd=2)
entry2.pack()
root.geometry('250x200')
btn=Button(root,text="Login",command=login)
btn.pack()
root.mainloop()
