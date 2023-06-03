from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]

    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_data():
    website = website_entry.get()
    username = username_entry.get()
    pass_word = password_entry.get()
    new_data = {website: {"email": username, "password": pass_word}}
    if len(website) != 0 and len(pass_word) != 0 and len(username) != 0:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, END)
            website_entry.focus()
        # messagebox.(title="Info",message="Information saved successfully")
    else:
        messagebox.showinfo(title="Oops", message="Entry fields cannot be empty!")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"email:{data[website]['email']}\npassword:"
                                                       f"{data[website]['password']}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the Website")

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("My Password Manager")

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="          Search          ", command=find_password)
search_button.grid(row=1, column=2)

username_entry = Entry(width=51)
username_entry.insert(0, "dileepkumarda3434@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=add_to_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
