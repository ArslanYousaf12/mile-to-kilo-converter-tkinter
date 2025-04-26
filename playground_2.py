from tkinter import *



# Creating a new windows and configuration

window = Tk()
window.title("This is window")
window.minsize(width=500, height=600)


# Labels
label = Label(text="This is label text", font=("Arial", 24, "bold"))
label.config(text="Lable changed")
label.pack()


# Button
def action():
    print("Button pressed")



# call action when button pressed
button = Button(text="click me", command=action)
button.pack()


# user input through entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
# entry.focus()
entry.pack()
value = entry.get()
print(value)


# Text

text = Text(height=20, width=20)
text.focus()
text.insert(END, "Example multi line text")
print(text.get("1.0", END))
text.pack()

#spinBox
def spinBox_used():
    print(spinBox.get())
    
spinBox = Spinbox(from_=0, to=100, command=spinBox_used)
spinBox.pack()

#Scale
def scale_used(value):
    print(value)
    
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()



#checkbox
def check_action():
    print(checkState.get())
    
checkState = IntVar()
checkbox = Checkbutton(text="IS NO", variable=checkState, command=check_action)
checkbox.pack()

#radio button
def radio_action():
    print(radio_state.get())
    
radio_state = IntVar()
radio_button_1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_action)
radio_button_2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_action)
radio_button_1.pack()
radio_button_2.pack()

#ListBox
def listbox_used():
    print(list_box.get(list_box.curselection()))
list_box = Listbox(height=4)
fruits = ["Apple", "banana", "Orange", "Pear"]
for item in fruits:
    list_box.insert(fruits.index(item), item)

list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()



window.mainloop()