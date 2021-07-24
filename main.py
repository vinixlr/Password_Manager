import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "" .join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_txt = entry_website.get()
    username_txt = entry_email.get()
    password_txt = entry_password.get()
    new_data = {
        website_txt: {
            "email": username_txt,
            "password": password_txt,
        }
    }

    if len(website_txt) == 0 or len(username_txt) == 0 or len(password_txt) == 0:
        messagebox.showinfo(title="Oops", message="Please don´t leave any fields empty !")
    else:
        try:
             with open ("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
             with open ("data.json", "w") as file:
                 json.dump(new_data, file , indent=4)
        else:
             with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_password.delete(0, 'end')

# ---------------------------- SEARCH ------------------------------- #

def search():
    website_txt = entry_website.get()

    try:
        with open ("data.json", "r") as file:
            search_file = json.load(file)
            messagebox.showinfo(title=website_txt, message=f"Email: {search_file[website_txt]['email']}\nPassword:"
                                                           f" {search_file[website_txt]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #

## Screen setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

## Canvas setup
canvas = tk.Canvas(width=200, height=200)
logo_png = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

## Labels
label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = tk.Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3)

## Entries
entry_website = tk.Entry(width=34)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_email = tk.Entry(width=53)
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = tk.Entry(width=34)
entry_password.grid(column=1, row=3)

## Buttons
button_generate = tk.Button(text="Generate  Password", command=password_generator)
button_generate.grid(column=2, row=3)
button_add = tk.Button(text="Add", width=45, command=save)
button_add.grid(column=1, row=4, columnspan=2)
button_search = tk.Button(text="Search", width=15, command=search)
button_search.grid(column=2, row=1)









window.mainloop()