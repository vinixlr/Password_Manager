import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

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

    if len(website_txt) == 0 or len(username_txt) == 0 or len(password_txt) == 0:
        messagebox.showinfo(title="Oops", message="Please don´t leave any fields empty !")
    else:

        is_ok = messagebox.askokcancel(title=website_txt, message=f"These are the details entered: \nEmail: {username_txt}\n"
                                    f"Password: {password_txt} \nIs it ok to save?")

        if is_ok:
            with open ("data.txt", "a") as file:
                file.write(f"{website_txt} | {username_txt} | {password_txt}\n")

            entry_website.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_password.delete(0, 'end')

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
entry_website = tk.Entry(width=53)
entry_website.grid(column=1, row=1, columnspan=2)
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









window.mainloop()