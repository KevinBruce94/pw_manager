import tkinter
from tkinter import *
from tkinter import messagebox
import random
import string
import pandas
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_clicked():
    length = 12
    password_entry.delete(0, END)
    characters = string.printable
    generate_password = "".join(random.choice(characters) for num in range(length))
    password_entry.insert(0, generate_password)
    pyperclip.copy(generate_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}" + "\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

#Creating window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", font=("Arial", 16, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Arial", 16, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 16, "bold"))
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hans@outlook.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="W")

#Buttons
generate_pw_button = Button(text="Generate Password", command=button_clicked)
generate_pw_button.grid(row=3, column=1, sticky="E")

add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)


window.mainloop()