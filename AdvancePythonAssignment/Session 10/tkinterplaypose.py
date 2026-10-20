import tkinter as tk

root = tk.Tk()
root.title("Music Player")

label = tk.Label(root, text="Select an action")
label.pack(pady=10)

def play():
    label.config(text="Playing")

def pause():
    label.config(text="Paused")

def next_song():
    label.config(text="Next Song")

tk.Button(root, text="Play", command=play).pack()
tk.Button(root, text="Pause", command=pause).pack()
tk.Button(root, text="Next", command=next_song).pack()

root.mainloop()