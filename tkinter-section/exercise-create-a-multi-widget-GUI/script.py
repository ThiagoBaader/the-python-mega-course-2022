# library import
from tkinter import *

# create an empty tkinter window
window = Tk()

# create the convertion function
def convert():
    # get user kg value from input box and convert to grams
    grams = float(e2.get()) * 1000
    # get user kg value from input box and convert to pounds
    pounds = float(e2.get()) * 2.20462
    # get user kg value from input box and convert to ounces
    ounces = float(e2.get()) * 35.274
    # empty the text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END) # deletes the content of the Text box from start to END
    t1.insert(END, grams) # fill in the text box with the value of grams variable
    t2.delete("1.0", END) # deletes the content of the Text box from start to END
    t2.insert(END, pounds) # fill in the text box with the value of pounds variable
    t3.delete("1.0", END) # deletes the content of the Text box from start to END
    t3.insert(END, ounces) # fill in the text box with the value of ounces variable

# create a label widget with "KG" as label
e1 = Label(window, text="kg")
e1.grid(row=0, column=0)

e2_value = StringVar() # create a special STringVar object
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# create a button widget
button = Button(window, text="Convert", command=convert)
button.grid(row=0, column=2)

# create three empty text boxes, t1, t2 and t3
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# this makes sure to keep the maind window open
window.mainloop()
