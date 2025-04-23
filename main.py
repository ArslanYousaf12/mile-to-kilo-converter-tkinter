import tkinter


window = tkinter.Tk()
window.title("This is my first Gui")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="This is label", font=("Arial", 26, "bold"))
my_label.pack(side="left")



window.mainloop()