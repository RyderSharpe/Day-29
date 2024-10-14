from tkinter import *
from datetime import datetime

DARK_PURPLE = "#522258"
LIGHT_PURPLE = "#8C3061"
RED = "#C63C51"
ORANGE = "#D95F59"
LOCK_COLOR = "#d4483b"
SCREEN_LENGTH_X = 200
SCREEN_LENGTH_Y = 200
FONT = ('Helvetica', 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save as: website | email | password
# Add button clears. ie. .delete(first, last=none)
# def add_save_button():
#     print("saved!")
#     with open('saved.txt', 'a') as file:
#         website_text = website_entry.get()
#         email_text = email_username_entry.get()
#         my_password_text = password_entry.get()
#         file.write(f"WEBSITE | EMAIL | PASSWORD\n")
#         file.write(f"{website_text} | {email_text} | {my_password_text}\n")
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)


def add_save_button():
    print("Saved!")

    # Get form data
    website_text = website_entry.get()
    email_text = email_username_entry.get()
    my_password_text = password_entry.get()

    # Validate form data
    if not website_text or not email_text or not my_password_text:
        print("Error: Please fill in all fields.")
        return

    # Save data to file
    with open('saved.txt', 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"----------------------------------------\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Website: {website_text}\n")
        file.write(f"Email: {email_text}\n")
        file.write(f"Password: {my_password_text}\n")
        file.write(f"----------------------------------------\n\n")

    # Clear form fields
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=LIGHT_PURPLE)

# LOGO Image
canvas = Canvas(width=200, height=200, bg=LIGHT_PURPLE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=(FONT), bg=LIGHT_PURPLE)
website_label.grid(column=0, row=1, sticky="e")
email_username_label = Label(text="Email/Username:", font=(FONT), bg=LIGHT_PURPLE)
email_username_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:", font=(FONT), bg=LIGHT_PURPLE)
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_entry = Entry(font=(FONT), width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = Entry(font=(FONT), width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_username_entry.insert(0, "rydersharpe@gmail.com")

password_entry = Entry(font=(FONT), show='*', width=21)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, width=16)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", highlightthickness=0, width=45, command=add_save_button)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
