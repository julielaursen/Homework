from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()

root.title("Swap Names")
root.geometry("400x150")
root.iconbitmap(r'./Green.ico')
root.iconbitmap(r'./Red.ico')

middleframe = Frame(root).pack(side=LEFT)
bottomframe = Frame(root).pack(side = BOTTOM)

def callback(*args):
   print("Entry now %s" % evar.get())

def swap(*args):
   #here's where i do some stuff to swap 

evar = StringVar()
evar2 = StringVar()
evar.trace("w", callback)
evar2.trace("w", callback)

label1 = Label(frame, text="First Name: ")
label1.pack(side=LEFT)
ent1 = Entry(frame, textvariable = evar).pack(side=LEFT)

label2 = Label(middleframe, text="Last Name: ", compound=CENTER)
label2.pack(side = LEFT)
ent2 = Entry(middleframe, textvariable = evar2).pack(side=LEFT)

#create swap button

btn = Button(bottomframe, text="Swap", bg='white').pack(side=BOTTOM)


root.mainloop()
