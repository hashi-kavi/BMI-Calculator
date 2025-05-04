import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        BMI = 10000 * (weight) / (height ** 2)

        if weight <= 0 or height <= 0:
            raise ValueError("Height and weight must be positive values.")
        if BMI < 16:
            state = "Severe Thinness"
        elif 16 <= BMI and BMI < 17:
            state = "Moderate Thinness"
        elif 17 <= BMI and BMI < 18.5:
            state = "Mild Thinness"
        elif 18.5 <= BMI and BMI < 25:
            state = "Normal"
        elif 25 <= BMI and BMI < 30:
            state = "Overweight"
        elif 30 <= BMI and BMI < 35:
            state = "Obese Class I"
        elif 35 <= BMI and BMI < 40:
            state = "Obese Class II"
        elif BMI > 40:
            state = "Obese Class III"
        result_label.config(
            text =f"{name}, you are {BMI:.2f} kg/m² ({state})"
        )
        result_label_1.config(text = "Healthy BMI range: 18.5 - 25 kg/m²")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")
def reset():
    name_entry.delete(0,tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    result_label_1.config(text="")

#gui setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x400")
root.config(bg="sky blue")

frame = tk.Frame(root, bg="sky blue")
frame.pack(expand=True)

title_label = tk.Label(frame,text="BMI Calculator", font=("Helvetica", 16, "bold"), bg="sky blue")
title_label.pack(pady=10)

tk.Label(frame, text ="Enter your name: ").pack(pady=5)
name_entry = tk.Entry(frame,bg="lightblue")
name_entry.pack(pady=5)

tk.Label(frame,text ="Enter your weight (kg) :").pack(pady=5)
weight_entry = tk.Entry(frame,bg="lightblue")
weight_entry.pack(pady=5)

tk.Label(frame,text ="Enter your height (cm):").pack(pady=5)
height_entry =tk.Entry(frame,bg="lightblue")
height_entry.pack(pady=5)

tk.Button(frame,text ="Calculate BMI",command =calculate_bmi).pack(pady =10)
tk.Button(frame,text ="Reset",command=reset,bg="lightcoral").pack(pady=5)

result_label =tk.Label(frame,text="",fg="blue",bg="sky blue")
result_label_1 =tk.Label(frame,text ="",fg="purple",bg="sky blue")
result_label.pack(pady=5)
result_label_1.pack(pady=5)

root.mainloop()

