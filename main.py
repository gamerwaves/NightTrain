from customtkinter import *
from tkinter import messagebox

class ScreenTimeManager:
    def __init__(self):
        self.points = 0
        self.day1 = ""
        self.day2 = ""
        self.day3 = ""
        self.day4 = ""
        self.day5 = ""
        self.limit = ""
        self.limitset_entry = ""
        self.limitlabel = ""
        

    def limitset(self):
        self.limit = int(self.limitset_entry.get().replace(":", ""))
        self.second.withdraw()
        self.window.deiconify()

    def set_times(self):
        self.day1 = int(self.day1_entry.get().replace(":",""))
        self.day2 = int(self.day2_entry.get().replace(":",""))
        self.day3 = int(self.day3_entry.get().replace(":",""))
        self.day4 = int(self.day4_entry.get().replace(":",""))
        self.day5 = int(self.day5_entry.get().replace(":",""))
        self.calculate_button.configure(state="normal")
        

    def calculate_points(self):
        if self.day1 and self.day2 and self.day3 and self.day4 and self.day5:
            if self.day1+self.day2+self.day3+self.day4+self.day5 <= self.limit*5:
                self.points += 500
                self.points_label.configure(text="Points: "+str(self.points))
                messagebox.showinfo("Congratulations!", "You earned 500 points for following your schedule!")
                self.calculate_button.configure(state="disabled")
            else:
                messagebox.showwarning("No.","You did not follow the schedule. You now only get 1 hour on the weekends.")
        else:
            messagebox.showwarning("Warning!", "Please set the amount you used your screen for first.")
    
    def double_screen_time(self):
        if self.points >= 1000 and self.points % 1000 == 0:
            self.points -= 1000
            messagebox.showinfo("Congratulations!", "You can now use your screen for double the time on weekends or show this to your parents for a treat!(like a cookie!!)")
            self.points_label.configure(text="Points: "+str(self.points))
        else:
            messagebox.showwarning("Sorry.","You do not have enough points to redeem a treat yet.")

    def create_window(self):
        self.window = CTk()
        self.window.withdraw()
        self.window.title("Screen Time Manager")
        keep_label = CTkLabel(self.window, text="Keep This App Open. Enter how much screen you use (HH:MM) everyday. Follow your schedule and you might get a treat!", font=("Helvetica", 18))
        keep_label.pack(padx=10, pady=10)

        self.second = CTk()
        self.second.title("Limit")
        self.second.geometry("200x200")

        limitset_label = CTkLabel(self.second, text="Set Screen Time Limit:")
        self.limitset_entry = CTkEntry(self.second)
        limitset_button = CTkButton(self.second, text="Set Limit", command=self.limitset)
        limitset_label.pack(pady=10)
        self.limitset_entry.pack(pady=10)
        limitset_button.pack(pady=10)

        day1_label = CTkLabel(self.window, text="Monday:")
        day1_label.pack()
        self.day1_entry = CTkEntry(self.window)
        self.day1_entry.pack()

        day2_label = CTkLabel(self.window, text="Tuesday:")
        day2_label.pack()
        self.day2_entry = CTkEntry(self.window)
        self.day2_entry.pack()

        day3_label = CTkLabel(self.window, text="Wensday:")
        day3_label.pack()
        self.day3_entry = CTkEntry(self.window)
        self.day3_entry.pack()

        
        day4_label = CTkLabel(self.window, text="Thursday:")
        day4_label.pack()
        self.day4_entry = CTkEntry(self.window)
        self.day4_entry.pack()
        
        day5_label = CTkLabel(self.window, text="Friday:")
        day5_label.pack()
        self.day5_entry = CTkEntry(self.window)
        self.day5_entry.pack()

        set_button = CTkButton(self.window, text="Set Times", command=self.set_times)
        set_button.pack(pady=10)

        self.calculate_button = CTkButton(self.window, text="Calculate Points", command=self.calculate_points,state="disabled")
        self.calculate_button.pack(pady=10)

        redeem_button = CTkButton(self.window, text="Redeem", command=self.double_screen_time)
        redeem_button.pack(pady=10)
        self.points_label = CTkLabel(self.window, text="Points: "+str(self.points))
        self.points_label.pack()

        self.window.mainloop()


manager = ScreenTimeManager()
manager.create_window()
