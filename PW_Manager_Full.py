from tkinter import *
from tkinter import messagebox
import customtkinter
from random import choice, randint, shuffle
from PIL import ImageTk, Image
import pyperclip
import json

LOGIN_FONT = "Roboto", 24, "bold"
BOLD_FONT = "Roboto", 18, "bold"
FONT = "Roboto", 16, "normal"
PW_FONT = "Roboto", 12, "normal"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    p_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    p_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = w_entry.get()
    email = e_entry.get()
    password = p_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            w_entry.delete(0, END)
            e_entry.delete(0, END)
            p_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
# appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# create window + frame
window = customtkinter.CTk()
window.title("Password Manager")
window.geometry("600x400")

frame = customtkinter.CTkFrame(master=window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# # insert logo
# logo = ImageTk.PhotoImage(Image.open("logo.png"))
# label = customtkinter.CTkLabel(master=frame, image=logo)
# label.grid(row=0, column=1, columnspan=2)

# labels
w_label = customtkinter.CTkLabel(master=frame, text="Website:", text_font=BOLD_FONT)
w_label.grid(row=0, column=0, padx=10, pady=10)
e_label = customtkinter.CTkLabel(master=frame, text="Email/Username:", text_font=BOLD_FONT)
e_label.grid(row=1, column=0, padx=10, pady=10)
p_label = customtkinter.CTkLabel(master=frame, text="Password:", text_font=BOLD_FONT)
p_label.grid(row=2, column=0, padx=10, pady=10)

# Entries
w_entry = customtkinter.CTkEntry(master=frame, text_font=FONT, width=350)
w_entry.grid(row=0, column=1, columnspan=2, padx=30)

e_entry = customtkinter.CTkEntry(master=frame, text_font=FONT, width=350)
e_entry.grid(row=1, column=1, columnspan=2, padx=30)

p_entry = customtkinter.CTkEntry(master=frame, text_font=PW_FONT, text=generate_password)
p_entry.grid(row=2, column=1, sticky=E, padx=20)

# button
generate_pw = customtkinter.CTkButton(master=frame, text="Generate Password", text_font=FONT, command=generate_password)
generate_pw.grid(row=2, column=2, sticky=W, padx=20)

add_button = customtkinter.CTkButton(master=frame, text="Add Password", text_font=FONT, width=150, command=save)
add_button.grid(row=3, column=1, columnspan=2, pady=10)



window.mainloop()
