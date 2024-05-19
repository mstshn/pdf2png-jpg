import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pdf2image import convert_from_path
import os

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_path.set(file_path)

def convert_to_images(format):
    pdf_file = pdf_path.get()
    if not pdf_file:
        messagebox.showwarning("Warning", "Please select a PDF file first!")
        return
    
    try:
        output_dir = filedialog.askdirectory()
        if not output_dir:
            return
        
        pages = convert_from_path(pdf_file)
        for i, page in enumerate(pages):
            output_path = os.path.join(output_dir, f'page_{i + 1}.{format}')
            page.save(output_path, format.upper())
        
        messagebox.showinfo("Success", f"PDF converted to {format.upper()} successfully!\nFiles saved in {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("PDF to Image Converter")

# Applying ttk theme
style = ttk.Style()
style.theme_use('clam')  # You can change this to 'default', 'classic', etc.

pdf_path = tk.StringVar()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame, text="Select PDF File:").grid(row=0, column=0, padx=5, pady=5, sticky='E')
ttk.Entry(frame, textvariable=pdf_path, width=50).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Browse", command=select_pdf).grid(row=0, column=2, padx=5, pady=5)

button_frame = ttk.Frame(root, padding="10")
button_frame.grid(row=1, column=0, pady=10)

ttk.Button(button_frame, text="Convert to PNG", command=lambda: convert_to_images('png')).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Convert to JPG", command=lambda: convert_to_images('jpg')).grid(row=0, column=1, padx=10)

# Center the window on the screen
root.update_idletasks()
win_width = root.winfo_width()
win_height = root.winfo_height()
x_pos = (root.winfo_screenwidth() // 2) - (win_width // 2)
y_pos = (root.winfo_screenheight() // 2) - (win_height // 2)
root.geometry(f"{win_width}x{win_height}+{x_pos}+{y_pos}")

root.mainloop()
