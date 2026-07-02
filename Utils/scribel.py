import os
import tkinter as tk
from tkinter import simpledialog, messagebox

def run_scribel():
    root = tk.Tk()
    root.title("PSR Scribel")
    root.geometry("600x400")
    root.resizable(False, False)

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    last_x, last_y = None, None

    def locate_xy(event):
        nonlocal last_x, last_y
        last_x, last_y = event.x, event.y

    def draw(event):
        nonlocal last_x, last_y
        if last_x and last_y:
            canvas.create_line(last_x, last_y, event.x, event.y, width=2, fill="black", capstyle=tk.ROUND, smooth=True)
        last_x, last_y = event.x, event.y

    def reset(event):
        nonlocal last_x, last_y
        last_x, last_y = None, None

    # Automatically exports and saves the drawing to the Vault on exit
    def save_and_close():
        filename = simpledialog.askstring("Save Drawing", "Enter canvas filename (e.g., drawing.ps):", parent=root)
        if filename:
            filename = filename.strip('\'"')
            if not filename.endswith('.ps'):
                filename += '.ps'
            try:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                vault_folder = os.path.join(base_dir, "Vault")
                os.makedirs(vault_folder, exist_ok=True)
                
                vault_path = os.path.join(vault_folder, filename)
                
                # Save canvas drawing vector data as a PostScript file
                canvas.postscript(file=vault_path, colormode='color')
                messagebox.showinfo("Saved", f"Canvas saved successfully to Vault as '{filename}'.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save drawing to Vault:\n{e}")
        root.destroy()

    canvas.bind("<Button-1>", locate_xy)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", reset)

    # Intercept window close event to trigger the save flow
    root.protocol("WM_DELETE_WINDOW", save_and_close)

    root.mainloop()