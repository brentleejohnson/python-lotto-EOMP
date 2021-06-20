# Brent Lee Johnson ==> Class 1
# End of Module Project
# Lottery Numbers


# Imports
from tkinter import *
from tkinter import messagebox
import uuid
from email_validator import validate_email, EmailNotValidError
import rsaidnumber
from dateutil import relativedelta
import datetime
# if on windows, use:
# import winsound
# on mac, use:
from playsound import playsound

window = Tk()
window.title("Registration")
window.geometry("350x250")
window.config(bg="#272640")


class Register:

    def __init__(self, root):
        # Heading
        self.registration_lbl1 = Label(root, text="Welcome To The Lotto Streak!!", fg="#006466")
        self.registration_lbl1.config(bg="#272640")
        self.registration_lbl1.place(x="65", y="0")

        self.registration_lbl2 = Label(root, text="To play, please sign-in below:", fg="#006466")
        self.registration_lbl2.config(bg="#272640")
        self.registration_lbl2.place(x="65", y="20")

        # Content
        # Name
        self.name_lbl = Label(root, text="Your Name:", fg="#006466")
        self.name_lbl.config(bg="#272640")
        self.name_lbl.place(x="40", y="61")

        self.name_entry = Entry(root)
        self.name_entry.config(bg="#4D194D", fg="#006466")
        self.name_entry.place(x="140", y="61")

        # Email
        self.email_lbl = Label(root, text="Email:", fg="#006466")
        self.email_lbl.config(bg="#272640")
        self.email_lbl.place(x="70", y="93")

        self.email_entry = Entry(root)
        self.email_entry.config(bg="#4D194D", fg="#006466")
        self.email_entry.place(x="140", y="93")

        # Id No.
        self.id_lbl = Label(root, text="Id No:", fg="#006466")
        self.id_lbl.config(bg="#272640")
        self.id_lbl.place(x="69", y="125")

        self.id_entry = Entry(root)
        self.id_entry.config(bg="#4D194D", fg="#006466")
        self.id_entry.place(x="140", y="125")

        self.register_btn = Button(root, text="Register", width="15", command=self.register_button)
        self.register_btn.place(x="95", y="180")

        # Footer
        self.footer_lbl = Label(root, text="Made by Brent Johnson", fg="#006466")
        self.footer_lbl.config(bg="#272640")
        self.footer_lbl.place(x="85", y="230")

    def register_button(self):
        try:
            # Email Validation
            email = self.email_entry.get()

            # Validate
            valid = validate_email(email)

            # Update with normalised form
            email = valid.email

            # Id No Validation
            int(self.id_entry.get())
            id = self.id_entry.get()
            date_of_birth = rsaidnumber.parse(id).date_of_birth

            if len(self.id_entry.get()) < 13 or len(self.id_entry.get()) > 13:
                raise ValueError
            elif relativedelta.relativedelta(datetime.datetime.today(), date_of_birth).years >= 18:
                messagebox.showinfo(message="Congratulations. You can now play!")
                window.destroy()
                import game
            else:
                messagebox.showerror(message="Excuse me young one. You are underage!")
        except EmailNotValidError as e:
            # Email is not valid, exception message
            messagebox.showerror("Email Validation", "Please check to ensure that your email is correct.")
        except ValueError:
            messagebox.showerror(message="Id number must be 13 digits.")


# Run the code
register = Register(window)
window.mainloop()
