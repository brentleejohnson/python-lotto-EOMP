# Brent Lee Johnson ==> Class1


import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import re
import datetime as dt
import requests
# Email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initialise the self
window = tk.Tk()
window.title("Lotto Machine")
window.geometry("900x400")
window.config(bg="#212F45")

class InvalidAccountName:
    pass

class Claim:
    def __init__(self, window):
        #  Heading
        self.label = Label(window, text="Enter your banking details", fg="black", bg="#212F45", font=("Garuda", 30)).pack()

        # Entries
        self.account_holder_name_entry = Entry(window)
        self.account_holder_name_entry.place(x=400, y=100)
        self.account_holder_name_label = Label(window, text="Account Holder Name", bg="#212F45", font=("Garuda", 13))
        self.account_holder_name_label.place(x=170, y=100)
        self.account_number_entry = Entry(window)
        self.account_number_entry.place(x=400, y=140)
        self.account_number_label = Label(window, text="Account Number", bg="#212F45", font=("Garuda", 13))
        self.account_number_label.place(x=170, y=140)
        self.variable = StringVar()
        self.variable.set('Select Bank')
        self.bank_opt = OptionMenu(window, self.variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
        self.bank_opt.place(x=630, y=100)
        self.currency_entry = Entry(window)
        self.currency_entry.place(x=400, y=180)
        self.currency_label = Label(window, text="Enter currency code", bg="#212F45", font=("Garuda", 13))
        self.currency_label.place(x=170, y=180)
        self.email_entry = Entry(window)
        self.email_entry.place(x=400, y=220)
        self.email_label = Label(window, text="Email", bg="#212F45", font=("Garuda", 13))
        self.email_label.place(x=170, y=220)

        # Email
        # sender_email_id = "brentleejohnson73@gmail.com"
        # receiver_email_id = ["naeemahndavis@gmail.com", "jasoncee017@gmail.com", "thapelo@lifechoices.co.za"]
        # password = input("Password: ")
        # Subject = "Testrun"
        # msg = MIMEMultipart()
        # msg['From'] = sender_email_id
        # msg['To'] = ", ".join(receiver_email_id)
        # msg['Subject'] = Subject
        # body = "Hey\n"
        # body = body + "Testing my coding for an email"
        # msg.attach(MIMEText(body, 'plain'))
        # text = msg.as_string()
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        #
        # # start TLS for security
        # s.starttls()
        #
        # # authentication
        # s.login(sender_email_id, password)
        #
        # # sending the mail
        # s.sendmail(sender_email_id, receiver_email_id, text)
        #
        # # s.sendmail(sender_email_id, receiver_email_id, text)
        #
        # # terminating the session
        # s.quit()


        # def send_message():
        #     email_body_info = email_body.get()
        #
        #     print(email_body_info)
        #
        #     sender_email = "jchno116012003@gmail.com"
        #
        #     sender_password = "googleaccount"
        #
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #
        #     server.starttls()
        #
        #     server.login(sender_email, sender_password)
        #
        #     print("Login successful")
        #
        #     server.sendmail(sender_email, email_body_info)
        #
        #     print("Message sent")

        def currency_converter():
            response = requests.get("https://v6.exchangerate-api.com/v6/f876d1e0093ad3e0efcfba54/latest/ZAR")
            data = response.json()
            with open("Login_use.txt", 'a') as file:
                for line in file:
                    if "Prize" in line:
                        prize = line[8:-1]
            total = prize
                # raise ValueError* data["conversion_rates"][self.currency_entry.get()]

        def enter():
            list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
            name_ent = self.account_holder_name_entry.get()
            number_ent = self.account_number_entry.get()
            with open("player_id.txt", "a+") as f:
                f.write("Account Holder Name: " + self.account_holder_name_entry.get() + "\n")
                f.write("Account Number: " + self.account_number_entry.get() + "\n")
                f.write("Currency Code: " + self.currency_entry.get() + "\n")
                f.write("Email: " + self.email_entry.get() + "\n")
            if name_ent == '':
                raise ValueError
            elif name_ent in list1:
                raise ValueError
            if number_ent == '':
                raise ValueError
            else:
                int(self.account_number_entry.get())
                messagebox.showinfo(message='Details have been entered correctly:)')
            if self.variable.get() == 'Select Bank':
                # raise ValueError
                messagebox.showwarning("enter a bank please")
            elif self.variable.get() == 'FNB':
                messagebox.showinfo(message='Details have been entered correctly:)')
            elif self.variable.get() == 'Capitec':
                messagebox.showinfo(message='Details have been entered correctly:)')
            elif self.variable.get() == 'Netbank':
                messagebox.showinfo(message='Details have been entered correctly:)')
            elif self.variable.get() == 'Standard Bank':
                messagebox.showinfo(message='Details have been entered correctly:)')
            try:
                int(self.account_number_entry.get())
                if self.account_holder_name_entry.get():
                    # writing to text file
                    # playsound("./sounds/391539__mativve__electro-win-sound.wav")
                    messagebox.showinfo("Thank You For Playing!", "Check your email for further instructions.")
                    # sending of email
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    sender_email_id = 'huntermoonspear@gmail.com'
                    receiver_email_id = self.email_entry.get()
                    password = 'dianadragonheart'

                    s.starttls()

                    s.login(sender_email_id, password)

                    message = "Subject: Congratulations!!!\n"
                    message = message + "Thank you for playing " + self.account_holder_name_entry.get() + "\nYour winnings are: " \
                  + "\nAccount name: " \
                  + self.account_holder_name_entry.get() + "\nAccount number: " + self.account_number_entry.get()
                    # + winningsLabel.cget('text') + "\nBelow are your details:" + "\nPlayer ID: " + playerID \
                    s.sendmail(sender_email_id, receiver_email_id, message)

                    s.quit()
                    # claimsc.destroy()
                    window.destroy()
            except ValueError:
                messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')

        # Buttons
        enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10, bg="#006466", fg="Black").place(x=280, y=300)
        exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10, bg="#006466", fg="Black").place(x=490, y=300)


# Running the program
Claim(window)
window.mainloop()
