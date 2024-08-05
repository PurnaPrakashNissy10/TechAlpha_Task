import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

# Main Window
root = tk.Tk()
root.title("Notes Application")
root.geometry("500x500")
style = Style(theme='journal')

# Tab Font
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Notebook to hold Notes
notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# For Loading Saved Notes
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

# To add New Notes
def add_note():
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")

    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10)

    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    # To save note
    def save_note():
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)

        if title.strip() == "":
            messagebox.showwarning("Warning", "Title cannot be empty!")
            return

        notes[title] = content.strip()

        with open("notes.json", "w") as f:
            json.dump(notes, f)

        # Add note to notebook
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(note_frame)
        notebook.add(note_content, text=title)

    # Save Button
    save_button = ttk.Button(note_frame, text="Save", command=save_note, style="secondary.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
            
        for title, content in notes.items():
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title) 

    except FileNotFoundError:
        pass 
    
load_notes()

def delete_note():
    current_tab = notebook.index(notebook.select())
    note_title = notebook.tab(current_tab, "text")

    confirm = messagebox.askyesno("Delete Note", f"Are you sure you want to delete {note_title}?")

    if confirm:
        notebook.forget(current_tab)
        notes.pop(note_title)
        with open("notes.json", "w") as f:
            json.dump(notes, f)

new_button = ttk.Button(root, text="New Note", command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
