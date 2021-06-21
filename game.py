# Brent Lee Johnson ==> Class1


from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Play lotto")
root.geometry("500x650")
root.config(bg="#272640")
root.resizable(0, 0)


class root_numbers:
    def __init__(self, lotto):
        self.lotto_lbl = Label(lotto, text="LOTTO STREAK!", font=("Garuda", 20))
        self.lotto_lbl.config(bg="#272640", fg="#006466")
        self.lotto_lbl.pack()
        self.btn1 = Button(lotto, text=1, width=2, command=lambda: self.on_click(1))
        self.btn1.place(x=50, y=85)
        self.btn2 = Button(lotto, text=2, width=2, command=lambda: self.on_click(2))
        self.btn2.place(x=100, y=85)
        self.btn3 = Button(lotto, text=3, width=2, command=lambda: self.on_click(3))
        self.btn3.place(x=150, y=85)
        self.btn4 = Button(lotto, text=4, width=2, command=lambda: self.on_click(4))
        self.btn4.place(x=200, y=85)
        self.btn5 = Button(lotto, text=5, width=2, command=lambda: self.on_click(5))
        self.btn5.place(x=250, y=85)
        self.btn6 = Button(lotto, text=6, width=2, command=lambda: self.on_click(6))
        self.btn6.place(x=300, y=85)
        self.btn7 = Button(lotto, text=7, width=2, command=lambda: self.on_click(7))
        self.btn7.place(x=350, y=85)

        # Next Line
        self.btn8 = Button(lotto, text=8, width=2, command=lambda: self.on_click(8))
        self.btn8.place(x=50, y=125)
        self.btn9 = Button(lotto, text=9, width=2, command=lambda: self.on_click(9))
        self.btn9.place(x=100, y=125)
        self.btn10 = Button(lotto, text=10, command=lambda: self.on_click(10))
        self.btn10.place(x=150, y=125)
        self.btn11 = Button(lotto, text=11, command=lambda: self.on_click(11))
        self.btn11.place(x=200, y=125)
        self.btn12 = Button(lotto, text=12, command=lambda: self.on_click(12))
        self.btn12.place(x=250, y=125)
        self.btn13 = Button(lotto, text=13, command=lambda: self.on_click(13))
        self.btn13.place(x=300, y=125)
        self.btn14 = Button(lotto, text=14, command=lambda: self.on_click(14))
        self.btn14.place(x=350, y=125)

        # Next Line
        self.btn15 = Button(lotto, text=15, command=lambda: self.on_click(15))
        self.btn15.place(x=50, y=165)
        self.btn16 = Button(lotto, text=16, command=lambda: self.on_click(16))
        self.btn16.place(x=100, y=165)
        self.btn17 = Button(lotto, text=17, command=lambda: self.on_click(17))
        self.btn17.place(x=150, y=165)
        self.btn18 = Button(lotto, text=18, command=lambda: self.on_click(18))
        self.btn18.place(x=200, y=165)
        self.btn19 = Button(lotto, text=19, command=lambda: self.on_click(19))
        self.btn19.place(x=250, y=165)
        self.btn20 = Button(lotto, text=20, command=lambda: self.on_click(20))
        self.btn20.place(x=300, y=165)
        self.btn21 = Button(lotto, text=21, command=lambda: self.on_click(21))
        self.btn21.place(x=350, y=165)

        # Next Line
        self.btn22 = Button(lotto, text=22, command=lambda: self.on_click(22))
        self.btn22.place(x=50, y=205)
        self.btn23 = Button(lotto, text=23, command=lambda: self.on_click(23))
        self.btn23.place(x=100, y=205)
        self.btn24 = Button(lotto, text=24, command=lambda: self.on_click(24))
        self.btn24.place(x=150, y=205)
        self.btn25 = Button(lotto, text=25, command=lambda: self.on_click(25))
        self.btn25.place(x=200, y=205)
        self.btn26 = Button(lotto, text=26, command=lambda: self.on_click(26))
        self.btn26.place(x=250, y=205)
        self.btn27 = Button(lotto, text=27, command=lambda: self.on_click(27))
        self.btn27.place(x=300, y=205)
        self.btn28 = Button(lotto, text=28, command=lambda: self.on_click(28))
        self.btn28.place(x=350, y=205)

        # Next Line
        self.btn29 = Button(lotto, text=29, command=lambda: self.on_click(29))
        self.btn29.place(x=50, y=245)
        self.btn30 = Button(lotto, text=30, command=lambda: self.on_click(30))
        self.btn30.place(x=100, y=245)
        self.btn31 = Button(lotto, text=31, command=lambda: self.on_click(31))
        self.btn31.place(x=150, y=245)
        self.btn32 = Button(lotto, text=32, command=lambda: self.on_click(32))
        self.btn32.place(x=200, y=245)
        self.btn33 = Button(lotto, text=33, command=lambda: self.on_click(33))
        self.btn33.place(x=250, y=245)
        self.btn34 = Button(lotto, text=34, command=lambda: self.on_click(34))
        self.btn34.place(x=300, y=245)
        self.btn35 = Button(lotto, text=35, command=lambda: self.on_click(35))
        self.btn35.place(x=350, y=245)

        # Next Line
        self.btn36 = Button(lotto, text=36, command=lambda: self.on_click(36))
        self.btn36.place(x=50, y=285)
        self.btn37 = Button(lotto, text=37, command=lambda: self.on_click(37))
        self.btn37.place(x=100, y=285)
        self.btn38 = Button(lotto, text=38, command=lambda: self.on_click(38))
        self.btn38.place(x=150, y=285)
        self.btn39 = Button(lotto, text=39, command=lambda: self.on_click(39))
        self.btn39.place(x=200, y=285)
        self.btn40 = Button(lotto, text=40, command=lambda: self.on_click(40))
        self.btn40.place(x=250, y=285)
        self.btn41 = Button(lotto, text=41, command=lambda: self.on_click(41))
        self.btn41.place(x=300, y=285)
        self.btn42 = Button(lotto, text=42, command=lambda: self.on_click(42))
        self.btn42.place(x=350, y=285)

        # Next Line
        self.btn43 = Button(lotto, text=43, command=lambda: self.on_click(43))
        self.btn43.place(x=50, y=325)
        self.btn44 = Button(lotto, text=44, command=lambda: self.on_click(44))
        self.btn44.place(x=100, y=325)
        self.btn45 = Button(lotto, text=45, command=lambda: self.on_click(45))
        self.btn45.place(x=150, y=325)
        self.btn46 = Button(lotto, text=46, command=lambda: self.on_click(46))
        self.btn46.place(x=200, y=325)
        self.btn47 = Button(lotto, text=47, command=lambda: self.on_click(47))
        self.btn47.place(x=250, y=325)
        self.btn48 = Button(lotto, text=48, command=lambda: self.on_click(48))
        self.btn48.place(x=300, y=325)
        self.btn49 = Button(lotto, text=49, command=lambda: self.on_click(49))
        self.btn49.place(x=350, y=325)

        # Next Line
        self.boardA = Label(lotto, width=25, height=2, bg="#4D194D", fg="#006466", cursor="dot")
        self.boardA.place(x=130, y=370)
        self.boardB = Label(lotto, width=25, height=2, bg="#4D194D", fg="#006466", cursor="dot")
        self.boardB.place(x=130, y=420)
        self.boardC = Label(lotto, width=25, height=2, bg="#4D194D", fg="#006466", cursor="dot")
        self.boardC.place(x=130, y=470)

        # Buttons
        self.play_btn = Button(lotto, text="Play", command=self.play)
        self.play_btn.place(x=15, y=600)
        self.claim_btn = Button(lotto, text="Claim Prize")
        self.claim_btn.place(x=200, y=600)
        self.replay_btn = Button(lotto, text="Play Again", command=self.play_again)
        self.replay_btn.place(x=415, y=600)
        self.lotto_no = Label(lotto, bg="#006466", fg="#4D194D")
        self.lotto_no.place(x=130, y=520)
        self.prizes_label = Label(lotto, bg="#006466", fg="#4D194D")
        self.prizes_label.place(x=130, y=540)
        self.root_set1 = []
        self.root_set2 = []
        self.root_set3 = []

    def on_click(self, pick):
        if len(self.root_set1) <= 5 and pick not in self.root_set1:
            self.root_set1.append(pick)
            self.boardA.config(text=self.root_set1)

        elif len(self.root_set1) == 6 and len(self.root_set2) <= 5 and pick not in self.root_set2:
            self.root_set2.append(pick)
            self.boardB.config(text=self.root_set2)

        elif len(self.root_set2) == 6 and len(self.root_set3) <= 5 and pick not in self.root_set3:
            self.root_set3.append(pick)
            self.boardC.config(text=self.root_set3)
        else:
            messagebox.showerror("Error", "You cannot pick anymore numbers")

    def play(self):
        correct = 0
        correct2 = 0
        correct3 = 0
        earnings1 = 0
        earnings2 = 0
        earnings3 = 0
        prizes = [0, 0, 20, 100.50, 2384, 8584, 10000000]
        lotto_list = random.sample(range(1, 49), 6)
        lotto_list.sort()
        matching1 = set(self.root_set1).intersection(set(lotto_list))
        matching2 = set(self.root_set2).intersection(set(lotto_list))
        matching3 = set(self.root_set3).intersection(set(lotto_list))
        for number in self.root_set1:
            if number in lotto_list:
                correct += 1
            if correct == 2:
                earnings1 = prizes[2]
            elif correct == 3:
                earnings1 = prizes[3]
            elif correct == 4:
                earnings1 = prizes[4]
            elif correct == 5:
                earnings1 = prizes[5]
            elif correct == 6:
                earnings1 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set 1: " + str(correct) + "\nEarnings: " + "R" + str(earnings1) +
                                 "\nMatching number: " + str(matching1))

        for number in self.root_set2:
            if number in lotto_list:
                correct2 += 1
            if correct2 == 2:
                earnings2 = prizes[2]
            elif correct2 == 3:
                earnings2 = prizes[3]
            elif correct2 == 4:
                earnings2 = prizes[4]
            elif correct2 == 5:
                earnings2 = prizes[5]
            elif correct2 == 6:
                earnings2 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set 2: " + str(correct2) + "\nEarnings: " +
                                 "R" + str(earnings2) + "\nMatching number: " + str(matching2))

        for number in self.root_set3:
            if number in lotto_list:
                correct3 += 1
            if correct3 == 2:
                earnings3 = prizes[2]
            elif correct3 == 3:
                earnings3 = prizes[3]
            elif correct3 == 4:
                earnings3 = prizes[4]
            elif correct3 == 5:
                earnings3 = prizes[5]
            elif correct3 == 6:
                earnings3 = prizes[6]
        else:
            messagebox.showerror("Matches", "Matches in set 3: " + str(correct3) + "\nEarnings: " +
                                 "R" + str(earnings3) + "\nMatching number: " + str(matching3))

        if len(self.root_set1) == 6 and len(self.root_set2) == 6 and len(self.root_set3) == 6:
            user_prize = float(earnings1 + earnings2 + earnings3)
            self.prizes_label.config(text="R" + str(user_prize))
            self.lotto_no.config(text=lotto_list)
        else:
            messagebox.showinfo("Error", "Please use all your tries first")

    def play_again(self):
        self.boardA.config(text="")
        self.boardB.config(text="")
        self.boardC.config(text="")
        self.prizes_label.config(text="")
        self.lotto_no.config(text="")
        self.root_set1 = []
        self.root_set2 = []
        self.root_set3 = []


numbers = root_numbers(root)
root.mainloop()
