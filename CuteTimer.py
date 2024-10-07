import tkinter as tk
from tkinter import messagebox
import time
import threading

# Funzione per avviare il timer con animazione
def start_timer():
    try:
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number!")
        return
    
    total_seconds = minutes * 60 + seconds
    
    def countdown():
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            #animate_label(timer_display)  # Aggiunge animazione ad ogni aggiornamento
            time.sleep(1)
        
        # Quando il tempo finisce
        label_timer.config(text="00:00")
        messagebox.showinfo("Time Expired", "🎉⏰ Time is up! Great work!")

    # Usa un thread separato per non bloccare l'interfaccia
    threading.Thread(target=countdown).start()

# Funzione per animare il cambio di orario
def animate_label(new_time):
    def grow():
        label_timer.config(font=("Arial", 60, "bold"))  # Aumenta la dimensione del font
        window.update()

    def shrink():
        label_timer.config(font=("Arial", 48, "bold"))  # Torna alla dimensione normale
        window.update()
    
    # Mostra l'orario attuale e applica l'animazione
    grow()
    label_timer.config(text=new_time)
    window.after(150, shrink)  # Torna alla dimensione normale dopo 150 ms

# Configura la finestra principale
window = tk.Tk()
window.title("Cute Timer")
window.geometry("600x250")
window.maxsize(width=600, height=250)
window.config(bg="#f5deb3")

# Stile
title_font = ("Comic Sans MS", 24, "bold")
label_font = ("Arial", 16)
button_font = ("Arial", 14, "bold")

# Etichetta del titolo
label_title = tk.Label(window, text=" 🍂 Cute Timer 🍂", font=title_font, fg="#8B4513", bg="#f5deb3")
label_title.pack(pady=5)

# Etichette e campi di input
frame_input = tk.Frame(window, bg="#f5deb3")
frame_input.pack(pady=3)

label_minutes = tk.Label(frame_input, text="Minutes:", font=label_font, bg="#f5deb3", fg="#8B4513")
label_minutes.grid(row=0, column=0, padx=5, pady=3)
entry_minutes = tk.Entry(frame_input, width=5, font=label_font, bg="#f5deb3")
entry_minutes.grid(row=0, column=1, padx=5, pady=3)

label_seconds = tk.Label(frame_input, text="Seconds:", font=label_font, bg="#f5deb3", fg="#8B4513")
label_seconds.grid(row=0, column=2, padx=5, pady=3)
entry_seconds = tk.Entry(frame_input, width=5, font=label_font, bg="#f5deb3")
entry_seconds.grid(row=0, column=3, padx=5, pady=3)

# Etichetta per il timer
label_timer = tk.Label(window, text="00:00", font=("Arial", 48, "bold"), fg="#ff8c00", bg="#f5deb3")
label_timer.pack(pady=3)

# Pulsanti
frame_buttons = tk.Frame(window, bg="#f5deb3")
frame_buttons.pack(pady=3)

button_start = tk.Button(frame_buttons, text="Start", font=button_font, bg="#32cd32", fg="white", command=start_timer)
button_start.grid(row=0, column=0, padx=5, pady=3)

button_quit = tk.Button(frame_buttons, text="Exit", font=button_font, bg="#ff4500", fg="white", command=window.quit)
button_quit.grid(row=0, column=1, padx=5, pady=3)

# Avvio del loop principale
window.mainloop()