import tkinter as tk

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

    canvas.bind("<Button-1>", locate_xy)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", reset)

    root.mainloop()