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
lotto_input_spin_1.place(x=20, y=70)

lotto_input_spin_2 = Spinbox(root, from_=0, to=49)
lotto_input_spin_2.config(width=2, font=("Garuda", 20))
lotto_input_spin_2.place(x=120, y=70)

lotto_input_spin_3 = Spinbox(root, from_=0, to=49)
lotto_input_spin_3.config(width=2, font=("Garuda", 20))
lotto_input_spin_3.place(x=220, y=70)

lotto_input_spin_4 = Spinbox(root, from_=0, to=49)
lotto_input_spin_4.config(width=2, font=("Garuda", 20))
lotto_input_spin_4.place(x=320, y=70)

lotto_input_spin_5 = Spinbox(root, from_=0, to=49)
lotto_input_spin_5.config(width=2, font=("Garuda", 20))
lotto_input_spin_5.place(x=420, y=70)

lotto_input_spin_6 = Spinbox(root, from_=0, to=49)
lotto_input_spin_6.config(width=2, font=("Garuda", 20))
lotto_input_spin_6.place(x=520, y=70)

# Answers
lotto_output_entry_1 = Entry(root)
lotto_output_entry_1.config(width=10)
lotto_output_entry_1.place(x=0, y=200)

lotto_output_entry_2 = Entry(root)
lotto_output_entry_2.config(width=10)
lotto_output_entry_2.place(x=100, y=200)

lotto_output_entry_3 = Entry(root)
lotto_output_entry_3.config(width=10)
lotto_output_entry_3.place(x=200, y=200)

lotto_output_entry_4 = Entry(root)
lotto_output_entry_4.config(width=10)
lotto_output_entry_4.place(x=300, y=200)

lotto_output_entry_5 = Entry(root)
lotto_output_entry_5.config(width=10)
lotto_output_entry_5.place(x=400, y=200)

lotto_output_entry_6 = Entry(root)
lotto_output_entry_6.config(width=10)
lotto_output_entry_6.place(x=500, y=200)

# Buttons
# Claim Button
lotto_claim_btn = Button(root, text="CLAIM")
lotto_claim_btn.config()
lotto_claim_btn.place()

# Play Again Button
lotto_play_again_btn = Button(root, text="PLAY AGAIN")
lotto_play_again_btn.config()
lotto_play_again_btn.place()

# Exit Button
lotto_exit_btn = Button(root, text="EXIT", command="exit")
lotto_exit_btn.config()
lotto_exit_btn.place()


# Run the code
root.mainloop()
