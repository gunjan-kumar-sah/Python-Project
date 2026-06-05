from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import psutil
import socket

# -------------------- SPLASH SCREEN -------------------- #

window1 = tk.Tk()
window1.title("Network Usage Tracker")
window1.geometry("1000x700")
window1.configure(bg="#0F172A")
window1.resizable(False, False)

title = Label(
    window1,
    text="NETWORK USAGE TRACKER",
    font=("Segoe UI", 34, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
)
title.pack(pady=30)

try:
    img = Image.open("Images/front.png")
    img = img.resize((400, 250))
    photo = ImageTk.PhotoImage(img)

    panel = Label(window1, image=photo, bg="#0F172A")
    panel.pack(pady=20)

except:
    pass


def start_fun():
    window1.destroy()


def exit_fun():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        window1.destroy()


Button(
    window1,
    text="START",
    command=start_fun,
    font=("Segoe UI", 18, "bold"),
    bg="#22C55E",
    fg="white",
    width=12
).place(x=220, y=600)

Button(
    window1,
    text="EXIT",
    command=exit_fun,
    font=("Segoe UI", 18, "bold"),
    bg="#EF4444",
    fg="white",
    width=12
).place(x=620, y=600)

window1.protocol("WM_DELETE_WINDOW", exit_fun)
window1.mainloop()

# -------------------- MAIN WINDOW -------------------- #

window = tk.Tk()
window.title("Network Usage Tracker")
window.geometry("1000x700")
window.configure(bg="#0F172A")
window.resizable(False, False)

# Header
Label(
    window,
    text="NETWORK USAGE TRACKER",
    font=("Segoe UI", 28, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
).pack(pady=20)

# Limit
Label(
    window,
    text="MAX LIMIT : 1 MB/sec",
    font=("Segoe UI", 20, "bold"),
    fg="#22C55E",
    bg="#0F172A"
).pack()

# Usage Frame
usage_frame = Frame(
    window,
    bg="#1E293B",
    bd=2,
    relief="ridge"
)
usage_frame.pack(pady=30, padx=40, fill="x")

usage_title = Label(
    usage_frame,
    text="Current Network Usage",
    font=("Segoe UI", 18, "bold"),
    bg="#1E293B",
    fg="white"
)
usage_title.pack(pady=10)

usage_label = Label(
    usage_frame,
    text="0 Bytes/sec",
    font=("Consolas", 28, "bold"),
    bg="#1E293B",
    fg="#FACC15"
)
usage_label.pack(pady=20)

# Connection Frame
status_frame = Frame(
    window,
    bg="#1E293B",
    bd=2,
    relief="ridge"
)
status_frame.pack(pady=20, padx=40, fill="x")

Label(
    status_frame,
    text="Connection Status",
    font=("Segoe UI", 18, "bold"),
    bg="#1E293B",
    fg="white"
).pack(pady=10)

status_label = Label(
    status_frame,
    text="Checking...",
    font=("Segoe UI", 18),
    bg="#1E293B",
    fg="#38BDF8"
)
status_label.pack(pady=20)

old_value = (
    psutil.net_io_counters().bytes_sent +
    psutil.net_io_counters().bytes_recv
)

alert_shown = False


def update_label():
    global old_value, alert_shown

    new_value = (
        psutil.net_io_counters().bytes_sent +
        psutil.net_io_counters().bytes_recv
    )

    usage = new_value - old_value

    usage_label.config(
        text=f"{usage:,} Bytes/sec"
    )

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)

        ip = socket.gethostbyname(
            socket.gethostname()
        )

        status_label.config(
            text=f"Connected\nIP Address : {ip}",
            fg="#22C55E"
        )

    except:
        status_label.config(
            text="No Internet Connection",
            fg="#EF4444"
        )

    if usage > 1000000 and not alert_shown:
        alert_shown = True

        messagebox.showwarning(
            "Bandwidth Alert",
            "Network usage exceeded 1 MB/sec"
        )

    if usage <= 1000000:
        alert_shown = False

    old_value = new_value

    window.after(1000, update_label)


def exit_main():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        window.destroy()


Button(
    window,
    text="EXIT",
    command=exit_main,
    font=("Segoe UI", 16, "bold"),
    bg="#EF4444",
    fg="white",
    width=12
).pack(pady=30)

window.protocol("WM_DELETE_WINDOW", exit_main)

update_label()

window.mainloop()