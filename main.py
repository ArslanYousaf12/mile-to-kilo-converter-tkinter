from tkinter import *


window = Tk()
window.title("This is my first Gui")
window.minsize(width=500, height=300)


my_label = Label(text="This is label", font=("Arial", 26, "bold"))
my_label.pack()

my_label["text"]= "New Text"
my_label.config(text="New Text")


#Button

def button_clicked():
    print("I Got clicked")
    input_value = input.get()
    my_label.config(text=input_value)
    

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()





window.mainloop()