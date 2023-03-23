from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, choice, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0 ,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = Email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "Email" : email,
            "Password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops !!!", message="Please make sure you didn't leave any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email : {email} \n Password : {password}")

        else:
            messagebox.showinfo(title="No Found", message=f"No Password saved for this {website}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=189)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
Email_lable = Label(text="Email/Username")
Email_lable.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
Email_entry = Entry(width=40)
Email_entry.grid(row=2, column=1, columnspan=2)
Email_entry.insert(0, "sharma999ansh@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_pass_button = Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()