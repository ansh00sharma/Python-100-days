from tkinter import *

window = Tk()
window.title("Mile to Kilo Converter")
window.minsize(200, 100)
window.config(padx=10, pady=10)

def mile_km():
    miles = float(miles_input.get())
    km = miles * 1.6
    kilo_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to ')
is_equal_label.grid(column=0, row=1)

kilo_label = Label(text='0')
kilo_label.grid(column=1, row=1)

km_label = Label(text='km')
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
