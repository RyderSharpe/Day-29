from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# LOGO Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

#Entries
website_Entry = Entry(width=35)
website_Entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="generate")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="add", width=36)
add_button.grid(row=4, column=1)

window.mainloop()
