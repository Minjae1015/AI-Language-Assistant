import tkinter as tk

window = tk.Tk()

window.title("AI Language Assistant")
window.geometry("600x500")

title = tk.Label(
    window,
    text="AI Language Assistant",
    font=("Arial", 24)
)

title.pack(pady=30)

window.mainloop()