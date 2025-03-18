import pytesseract
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, Text
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import threading

def extract_text(image_path):
    loading_label.config(text="Processing...", foreground="gray")
    root.update_idletasks()
    
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        text_output.delete("1.0", "end")
        text_output.insert("1.0", text)
    except Exception as e:
        text_output.delete("1.0", "end")
        text_output.insert("1.0", f"Error: {str(e)}")
    
    loading_label.config(text="Drag & Drop an Image Here", foreground="Black")

def drop(event):
    file_path = event.data.replace('{', '').replace('}', '')  # Fix path formatting
    threading.Thread(target=extract_text, args=(file_path,), daemon=True).start()

# GUI Setup
root = TkinterDnD.Tk()  # Enable drag-and-drop
root.title("OCR Drag & Drop App")
root.geometry("600x450")
root.configure(bg="#222222")  # Dark gray background

# Loading Label
loading_label = ttk.Label(root, text="Drag & Drop an Image Here", bootstyle="light-inverse", font=("Arial", 14))
loading_label.pack(pady=20)

# Drag-and-Drop Area
drop_area = ttk.Label(root, text="Drop Image Here", bootstyle="secondary-inverse", width=50, anchor="center", font=("Arial", 12), background="#333333", foreground="white", padding=10)
drop_area.pack(pady=15)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind("<<Drop>>", drop)

# Text Output
text_output = Text(root, height=10, wrap="word", font=("Arial", 12), bg="#111111", fg="white", insertbackground="white")
text_output.pack(pady=10, padx=10, fill="both", expand=True)

root.mainloop()

