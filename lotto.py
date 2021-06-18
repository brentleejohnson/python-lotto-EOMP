# Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
# from playsound import playsound

root = Tk()
root.title("Lotto Streak!")
root.geometry("450x500")
root.config(bg="#343434")

# Heading
lotto_lbl = Label(root, text="Lotto Streak!!", fg="#7A7A7A")
lotto_lbl.config(bg="#343434", font=("Garuda", 20))
lotto_lbl.pack()


# Content
# Input
lotto_input_spin_1 = tk.Spinbox(root, from_=0, to=49)
lotto_input_spin_1.config(width=2, font=("Garuda", 20))
lotto_input_spin_1.place(x=150, y=70)

lotto_input_spin_2 = Spinbox(root, from_=0, to=49)
lotto_input_spin_2.config(width=2, font=("Garuda", 20))
lotto_input_spin_2.place(x=225, y=70)

lotto_input_spin_3 = Spinbox(root, from_=0, to=49)
lotto_input_spin_3.config(width=2, font=("Garuda", 20))
lotto_input_spin_3.place(x=300, y=80)

lotto_input_spin_4 = Spinbox(root, from_=0, to=49)
lotto_input_spin_4.config(width=2, font=("Garuda", 20))
lotto_input_spin_4.place(x=370, y=120)

lotto_input_spin_5 = Spinbox(root, from_=0, to=49)
lotto_input_spin_5.config(width=2, font=("Garuda", 20))
lotto_input_spin_5.place(x=390, y=190)

lotto_input_spin_6 = Spinbox(root, from_=0, to=49)
lotto_input_spin_6.config(width=2, font=("Garuda", 20))
lotto_input_spin_6.place(x=395, y=260)


# Answers
answ_frame = Frame(root, width=320, height=140)
answ_frame.config()
answ_frame.place(x=20, y=165)


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
            # Supposed to add the ouput to output_entries

        # Storage for the lists
        matching_numbers = set(user_list) & set(lotto_numbers)
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
lotto_play_again_btn.place(x=180, y=465)

# Exit Button
lotto_exit_btn = Button(root, text="EXIT", command="exit")
lotto_exit_btn.config()
lotto_exit_btn.place(x=385, y=465)


# Run the code
root.mainloop()
