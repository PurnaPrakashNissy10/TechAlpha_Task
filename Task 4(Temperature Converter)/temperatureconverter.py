import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        if selected_conversion.get() == 'F to C':
            result = fahrenheit_to_celsius(temp)
            result_label.config(text=f"{temp:.2f}°F is {result:.2f}°C")
        else:
            result = celsius_to_fahrenheit(temp)
            result_label.config(text=f"{temp:.2f}°C is {result:.2f}°F")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Main Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x200")

# Temperature Entry
entry_frame = ttk.Frame(root, padding=(10, 10))
entry_frame.pack(fill=tk.X, pady=(10, 0))

entry_label = ttk.Label(entry_frame, text="Enter Temperature:")
entry_label.pack(side=tk.LEFT, padx=(0, 10))

entry_temp = ttk.Entry(entry_frame)
entry_temp.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Conversion Type
conversion_frame = ttk.Frame(root, padding=(10, 10))
conversion_frame.pack(fill=tk.X, pady=(10, 0))

conversion_label = ttk.Label(conversion_frame, text="Convert:")
conversion_label.pack(side=tk.LEFT, padx=(0, 10))

selected_conversion = tk.StringVar(value='F to C')
conversion_options = ttk.Combobox(conversion_frame, textvariable=selected_conversion, values=['F to C', 'C to F'])
conversion_options.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Convert Button
button_frame = ttk.Frame(root, padding=(10, 10))
button_frame.pack(fill=tk.X, pady=(10, 0))

convert_button = ttk.Button(button_frame, text="Convert", command=convert_temperature)
convert_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Result Label
result_label = ttk.Label(root, text="Result will be shown here", padding=(10, 10))
result_label.pack(fill=tk.X, pady=(10, 0))

# Start the main event loop
root.mainloop()
