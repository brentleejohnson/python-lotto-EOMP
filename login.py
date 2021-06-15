# Brent Lee Johnson ==> Class 1
# End of Module Project
# Lottery Numbers


# Imports
from tkinter import *
from tkinter import messagebox
# if on windows, use:
import winsound
# on mac, use:
# from playsound import playsound

root = Tk()
root.title("Registration")
root.geometry("300x300")
root.config(bg="#343434")

# Heading
registration_lbl1 = Label(root, text="Welcome To The Lotto Streak!!", fg="#7A7A7A")
registration_lbl1.config(bg="#343434")
registration_lbl1.pack()

registration_lbl2 = Label(root, text="To play, please sign-in below:", fg="#7A7A7A")
registration_lbl2.config(bg="#343434")
registration_lbl2.pack()

# Content
# Name
name_lbl = Label(root, text="Your Name:", fg="#7A7A7A")
name_lbl.config(bg="#343434")
name_lbl.pack()

name_entry = Entry(root)
name_entry.config()
name_entry.pack()

# Email
email_lbl = Label(root, text="Email:", fg="#7A7A7A")
email_lbl.config(bg="#343434")
email_lbl.pack()

email_entry = Entry(root)
email_entry.config()
email_entry.pack()

# Id No.
id_lbl = Label(root, text="Id No.:", fg="#7A7A7A")
id_lbl.config(bg="#343434")
id_lbl.pack()

id_entry = Entry(root)
id_entry.config()
id_entry.pack()

# Footer
footer_lbl = Label(root, text="Made by Brent Johnson", fg="#7A7A7A")
footer_lbl.config(bg="#343434")
footer_lbl.pack()


# Run the code
root.mainloop()
