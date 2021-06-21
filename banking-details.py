# Brent Lee Johnson ==> Class1


import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests

# initialise the root
root = Tk()
root.title("Lotto Machine: Jayden May")
root.geometry("900x600")
root.config(bg="yellow")

#  Heading
label = Label(root, text="Enter your banking details", fg="black", bg="yellow", font=("Arial", 20)).place(x=300, y=200)

# Entries
account_holder_name_entry = Entry(root)
account_holder_name_entry.place(x=400, y=300)
account_holder_name_label = Label(root, text="Account Holder Name", bg="yellow", font=("Arial", 13))
account_holder_name_label.place(x=170, y=300)
account_number_entry = Entry(root)
account_number_entry.place(x=400, y=340)
account_number_label = Label(root, text="Account Number", bg="yellow", font=("Arial", 13))
account_number_label.place(x=170, y=340)
variable = StringVar()
variable.set('Select Bank')
bank_opt = OptionMenu(root, variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
bank_opt.place(x=630, y=300)
currency_entry = Entry(root)
currency_entry.place(x=400, y=380)
currency_label = Label(root, text="Enter currency code", bg="yellow", font=("Arial", 13))
currency_label.place(x=170, y=380)
email_entry = Entry(root)
email_entry.place(x=400, y=420)
email_label = Label(root, text="Email", bg="yellow", font=("Arial", 13))
email_label.place(x=170, y=420)

def currency_converter():
    response = requests.get("https://v6.exchangerate-api.com/v6/f876d1e0093ad3e0efcfba54/latest/ZAR")
    data = response.json()
    with open("Login_use.txt", 'a') as file:
        for line in file:
            if "Prize" in line:
                prize = line[8:-1]
    total = prize * data["conversion_rates"][currency_entry.get()]


# Function to tells if user is older enough to play
def enter():
    try:
        list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
        name_ent = account_holder_name_entry.get()
        number_ent = account_number_entry.get()
        if name_ent == '':
            raise ValueError
        elif name_ent in list1:
            raise ValueError
        if number_ent == '':
            raise ValueError
        else:
            int(account_number_entry.get())
            messagebox.showinfo(message='Details have been entered correctly:)')
        if variable.get() == 'Select Bank':
            raise ValueError
        elif variable.get() == 'FNB':
            messagebox.showinfo(message='Details have been entered correctly:)')
        elif variable.get() == 'Capitec':
            messagebox.showinfo(message='Details have been entered correctly:)')
        elif variable.get() == 'Netbank':
            messagebox.showinfo(message='Details have been entered correctly:)')
        elif variable.get() == 'Standard Bank':
            messagebox.showinfo(message='Details have been entered correctly:)')
    except ValueError:
        messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')


# Buttons
enter_button = tk.Button(root, text="Enter", command=enter, height=2, width=10, bg="Green").place(x=280, y=500)
exit_button = tk.Button(root, text="Exit", command=exit, height=2, width=10, bg="red").place(x=490, y=500)


# Running the program
root.mainloop()
