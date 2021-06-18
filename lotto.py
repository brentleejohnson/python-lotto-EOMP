# Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
# from playsound import playsound

root = Tk()
root.title("Lotto Streak!")
root.geometry("600x500")
root.config(bg="#343434")

# Heading
lotto_lbl = Label(root, text="Lotto Streak!!", fg="#7A7A7A")
lotto_lbl.config(bg="#343434", font=("Garuda", 20))
lotto_lbl.pack()


# Content
# Input
lotto_input_spin_1 = tk.Spinbox(root, from_=0, to=49)
lotto_input_spin_1.config(width=2, font=("Garuda", 20))
lotto_input_spin_1.place(x=20, y=70)

lotto_input_spin_2 = Spinbox(root, from_=0, to=49)
lotto_input_spin_2.config(width=2, font=("Garuda", 20))
lotto_input_spin_2.place(x=120, y=90)

lotto_input_spin_3 = Spinbox(root, from_=0, to=49)
lotto_input_spin_3.config(width=2, font=("Garuda", 20))
lotto_input_spin_3.place(x=220, y=110)

lotto_input_spin_4 = Spinbox(root, from_=0, to=49)
lotto_input_spin_4.config(width=2, font=("Garuda", 20))
lotto_input_spin_4.place(x=320, y=130)

lotto_input_spin_5 = Spinbox(root, from_=0, to=49)
lotto_input_spin_5.config(width=2, font=("Garuda", 20))
lotto_input_spin_5.place(x=420, y=150)

lotto_input_spin_6 = Spinbox(root, from_=0, to=49)
lotto_input_spin_6.config(width=2, font=("Garuda", 20))
lotto_input_spin_6.place(x=520, y=170)


# Answers
lotto_output_entry_1 = Entry(root, state="disable")
lotto_output_entry_1.config(width=4, font=("Garuda", 15))
lotto_output_entry_1.place(x=20, y=200)

lotto_output_entry_2 = Entry(root, state="disable")
lotto_output_entry_2.config(width=4, font=("Garuda", 15))
lotto_output_entry_2.place(x=120, y=220)

lotto_output_entry_3 = Entry(root, state="disable")
lotto_output_entry_3.config(width=4, font=("Garuda", 15))
lotto_output_entry_3.place(x=220, y=240)

lotto_output_entry_4 = Entry(root, state="disable")
lotto_output_entry_4.config(width=4, font=("Garuda", 15))
lotto_output_entry_4.place(x=320, y=260)

lotto_output_entry_5 = Entry(root, state="disable")
lotto_output_entry_5.config(width=4, font=("Garuda", 15))
lotto_output_entry_5.place(x=420, y=280)

lotto_output_entry_6 = Entry(root, state="disable")
lotto_output_entry_6.config(width=4, font=("Garuda", 15))
lotto_output_entry_6.place(x=520, y=300)


# Amount of Plays Left
plays_left_lbl = Label(root)
plays_left_lbl.config()
plays_left_lbl.place()

# List of users' numbers
user_list = []

# Lotto numbers
lotto_numbers = random.sample(range(0, 49), 6)
print(lotto_numbers)


# Lotto Draw Function
def lotto():
    # Getting users' inputs
    try:
        user_list = [int(lotto_input_spin_1.get()), int(lotto_input_spin_2.get()),
                     int(lotto_input_spin_3.get()), int(lotto_input_spin_4.get()),
                     int(lotto_input_spin_5.get()), int(lotto_input_spin_6.get())]

        for i in range(6):
            if 0 <= int(user_list[i]) <= 49:
                user_list.append(user_list[i])
            elif 49 < int(user_list[i]):
                messagebox.showerror("Error", "Enter numbers between 0-49")

    except:
        messagebox.show('error')


# Buttons
# Claim Button
lotto_claim_btn = Button(root, text="CLAIM")
lotto_claim_btn.config()
lotto_claim_btn.place(x=5, y=465)

# Play Again Button
lotto_play_again_btn = Button(root, text="PLAY AGAIN")
lotto_play_again_btn.config()
lotto_play_again_btn.place(x=260, y=465)

# Exit Button
lotto_exit_btn = Button(root, text="EXIT", command="exit")
lotto_exit_btn.config()
lotto_exit_btn.place(x=535, y=465)


# Run the code
root.mainloop()
