import tkinter

FONT = ("Arial", 18, "normal")
window = tkinter.Tk()
window.title("Miles to km calculator")

# Label
my_label = tkinter.Label( width=10)
my_label.grid(row=0, column=0)

# Entry
my_entry = tkinter.Entry(width=10)
my_entry.grid(row=0, column=1)

miles = tkinter.Label(text="miles", font=FONT)
miles.grid(row=0, column=2)

equal = tkinter.Label(text="is equal to", font=FONT)
equal.grid(row=1, column=0)

sum_input = tkinter.Label(text=0, font=FONT)
sum_input.grid(row=1, column=1)

km = tkinter.Label(text="Km", font=FONT)
km.grid(row=1, column=2)


def calculation():
    new_input = my_entry.get()
    int_input = int(new_input)
    sum_of_all = round(int_input * 1.6)
    sum_input.config(text=sum_of_all)


button = tkinter.Button(text="Calculate", command=calculation)
button.grid(row=2,column=1)

window.mainloop()
