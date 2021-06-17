# Imports
from tkinter import *
import tkinter as tk
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
lotto_input_spin_1.pack()

lotto_input_spin_2 = Spinbox(root, from_=0, to=49)
lotto_input_spin_2.config(width=2, font=("Garuda", 20))
lotto_input_spin_2.pack()

lotto_input_spin_3 = Spinbox(root, from_=0, to=49)
lotto_input_spin_3.config(width=2, font=("Garuda", 20))
lotto_input_spin_3.pack()

lotto_input_spin_4 = Spinbox(root, from_=0, to=49)
lotto_input_spin_4.config(width=2, font=("Garuda", 20))
lotto_input_spin_4.pack()

lotto_input_spin_5 = Spinbox(root, from_=0, to=49)
lotto_input_spin_5.config(width=2, font=("Garuda", 20))
lotto_input_spin_5.pack()

lotto_input_spin_6 = Spinbox(root, from_=0, to=49)
lotto_input_spin_6.config(width=2, font=("Garuda", 20))
lotto_input_spin_6.pack()

# Answers
lotto_output_entry_1 = Entry(root)
lotto_output_entry_1.config()
lotto_output_entry_1.pack()

lotto_output_entry_2 = Entry(root)
lotto_output_entry_2.config()
lotto_output_entry_2.pack()

lotto_output_entry_3 = Entry(root)
lotto_output_entry_3.config()
lotto_output_entry_3.pack()

lotto_output_entry_4 = Entry(root)
lotto_output_entry_4.config()
lotto_output_entry_4.pack()

lotto_output_entry_5 = Entry(root)
lotto_output_entry_5.config()
lotto_output_entry_5.pack()

lotto_output_entry_6 = Entry(root)
lotto_output_entry_6.config()
lotto_output_entry_6.pack()

# Buttons
# Claim Button
lotto_claim_btn = Button(root, text="CLAIM")
lotto_claim_btn.config()
lotto_claim_btn.pack()

# Play Again Button
lotto_play_again_btn = Button(root, text="PLAY AGAIN")
lotto_play_again_btn.config()
lotto_play_again_btn.pack()

# Exit Button
lotto_exit_btn = Button(root, text="EXIT")
lotto_exit_btn.config()
lotto_exit_btn.pack()


# Run the code
root.mainloop()
