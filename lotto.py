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
lotto_input_entry_1 = Entry(root)
lotto_input_entry_1.config(width=2, font=("Garuda", 20))
lotto_input_entry_1.place(x=75, y=70)

lotto_input_entry_2 = Entry(root)
lotto_input_entry_2.config(width=2, font=("Garuda", 20))
lotto_input_entry_2.place(x=215, y=70)

lotto_input_entry_3 = Entry(root)
lotto_input_entry_3.config(width=2, font=("Garuda", 20))
lotto_input_entry_3.place(x=335, y=70)

lotto_input_entry_4 = Entry(root)
lotto_input_entry_4.config(width=2, font=("Garuda", 20))
lotto_input_entry_4.place(x=75, y=165)

lotto_input_entry_5 = Entry(root)
lotto_input_entry_5.config(width=2, font=("Garuda", 20))
lotto_input_entry_5.place(x=215, y=165)

lotto_input_entry_6 = Entry(root)
lotto_input_entry_6.config(width=2, font=("Garuda", 20))
lotto_input_entry_6.place(x=335, y=165)


# Amount of Plays Left
plays_left_lbl = Label(root)
plays_left_lbl.config()
plays_left_lbl.place()

# List of users' numbers
user_list = []

# Lotto numbers
lotto_numbers = random.sample(range(0, 49), 6)


# Lotto Draw Function
def lotto():
    # Getting users' inputs
    try:
        user_list = [int(lotto_input_entry_1.get()), int(lotto_input_entry_2.get()),
                     int(lotto_input_entry_3.get()), int(lotto_input_entry_4.get()),
                     int(lotto_input_entry_5.get()), int(lotto_input_entry_6.get())]

        for i in range(6):
            if 0 <= int(user_list[i]) <= 49:
                user_list.append(user_list[i])
            elif 49 < int(user_list[i]):
                messagebox.showerror("Error", "Enter numbers between 0-49")
            lotto_numbers_lbl = Label(root, text=lotto_numbers, font=("Garuda", 15))
            lotto_numbers_lbl.place(x=20, y=250)

        # Storage for the lists
        matched_numbers = set(user_list) & set(lotto_numbers)

        if user_list == user_list:
            matched_numbers_lbl = Label(root, text=matched_numbers, font=("Garuda", 15))
            matched_numbers_lbl.place(x=20, y=280)
        else:
            if user_list == 00:
                messagebox.showerror("Try Again", "There aren't any matched numbers:(")

        if len(matched_numbers) == 0:
            matching_label = Label(root, text="0", font=("Garuda", 15))
            matching_label.place(x=20, y=310)
            messagebox.showerror("Try Again", "There aren't any matched numbers:(")

        elif len(matched_numbers) == 1:
            messagebox.showerror("Tough Luck", "You only matched one number, try again")
        elif len(matched_numbers) == 2:
            messagebox.showinfo("Nice!", "You won R20.00")
        elif len(matched_numbers) == 3:
            messagebox.showinfo("NICE!!", "You won R100.50")
        elif len(matched_numbers) == 4:
            messagebox.showinfo("Amazing!", "You won R384.00")
        elif len(matched_numbers) == 5:
            messagebox.showinfo("FABULOUS!!", "You won R8 584.00")
        elif len(matched_numbers) == 6:
            messagebox.showinfo("Congratulations Champion!", "You won R10 000 000.00")

    except ValueError:
        messagebox.showerror("Enter your numbers to play")


# Buttons
# Claim Button
lotto_claim_btn = Button(root, text="CLAIM")
lotto_claim_btn.config()
lotto_claim_btn.place(x=5, y=465)

# Play Again Button
lotto_play_again_btn = Button(root, text="PLAY", command=lotto)
lotto_play_again_btn.config()
lotto_play_again_btn.place(x=180, y=465)

# Exit Button
lotto_exit_btn = Button(root, text="EXIT", command="exit")
lotto_exit_btn.config()
lotto_exit_btn.place(x=385, y=465)


# Run the code
root.mainloop()
