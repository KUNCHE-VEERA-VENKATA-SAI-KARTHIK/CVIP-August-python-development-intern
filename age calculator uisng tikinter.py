import tkinter as tk
from datetime import date

def calculate_age():
    birth_year = int(entry_year.get())
    birth_month = int(entry_month.get())
    birth_day = int(entry_day.get())
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    label_age.config(text=f"Your age is: {age}")

window = tk.Tk()
window.title("Age Calculator")

label_year = tk.Label(text="Year:")
label_month = tk.Label(text="Month:")
label_day = tk.Label(text="Day:")

entry_year = tk.Entry()
entry_month = tk.Entry()
entry_day = tk.Entry()

button_calculate = tk.Button(text="Calculate Age", command=calculate_age)
label_age = tk.Label(text="Your age is:")

label_year.grid(row=0, column=0)
entry_year.grid(row=0, column=1)
label_month.grid(row=1, column=0)
entry_month.grid(row=1, column=1)
label_day.grid(row=2, column=0)
entry_day.grid(row=2, column=1)
button_calculate.grid(row=3, column=0)
label_age.grid(row=4, column=0)

window.mainloop()
