import tkinter as tk
from tkinter import messagebox
import time 
import threading
from BtnFun import (hideButton, startButton)
from PIL import Image, ImageTk
from themes import themes



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
        hideButton(button_start)
        hideButton(label_minutes)
        hideButton(entry_minutes)
        hideButton(label_seconds)
        hideButton(entry_seconds)
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            animate_label(timer_display)  # Aggiunge animazione ad ogni aggiornamento
            time.sleep(1)
        
        # Quando il tempo finisce
        startButton(button_start)
        startButton(label_minutes)
        startButton(entry_minutes)
        startButton(label_seconds)
        startButton(entry_seconds)
        label_timer.config(text="00:00")
        messagebox.showinfo("Time Expired", "🎉⏰ Time is up! Great work!")

    # Usa un thread separato per non bloccare l'interfaccia
    threading.Thread(target=countdown).start()

# Funzione per animare il cambio di orario
def animate_label(new_time):
    def grow():
        label_timer.config(font=("Arial", 48, "bold"))  # Aumenta la dimensione del font
        window.update()

    def shrink():
        #label_timer.config(font=("Arial", 48, "bold"))  # Torna alla dimensione normale
        window.update()
    
    # Mostra l'orario attuale e applica l'animazione
    grow()
    label_timer.config(text=new_time)
    window.after(150, shrink)  # Torna alla dimensione normale dopo 150 
    

    # Funzione per applicare il tema autunnale
def apply_theme(theme):
    window.config(bg=theme["bg"])
    label_title.config(fg=theme["fg_title"], bg=theme["bg"], font=theme["font_title"])
    label_minutes.config(fg=theme["fg_label"], bg=theme["bg"], font=theme["font_label"])
    entry_minutes.config(bg=theme["entry_bg"], fg=theme["entry_fg"], font=theme["font_label"])
    label_seconds.config(fg=theme["fg_label"], bg=theme["bg"], font=theme["font_label"])
    entry_seconds.config(bg=theme["entry_bg"], fg=theme["entry_fg"], font=theme["font_label"])
    label_timer.config(fg=theme["fg_timer"], bg=theme["bg"], font=theme["font_timer"])
    button_start.config(bg=theme["button_start_bg"], fg=theme["button_start_fg"], font=theme["font_button"])
    button_quit.config(bg=theme["button_quit_bg"], fg=theme["button_quit_fg"], font=theme["font_button"])


# Crea la finestra principale
window = tk.Tk()
window.title("🍂 Cute Timer 🍂")
window.geometry("600x300")

# Etichetta del titolo
label_title = tk.Label(window, text="🍂 Cute Timer 🍂")
label_title.pack(pady=5)

# Etichette e campi di input per il tempo (minuti e secondi)
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_minutes = tk.Label(frame_input, text="Minutes:")
label_minutes.grid(row=0, column=0, padx=10)
entry_minutes = tk.Entry(frame_input, width=5, justify="center")
entry_minutes.grid(row=0, column=1, padx=5)

label_seconds = tk.Label(frame_input, text="Seconds:")
label_seconds.grid(row=0, column=2, padx=10)
entry_seconds = tk.Entry(frame_input, width=5, justify="center")
entry_seconds.grid(row=0, column=3, padx=5)

# Etichetta per il timer
label_timer = tk.Label(window, text="00:00")
label_timer.pack(pady=20)

# Pulsanti di controllo (Start e Exit)
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

button_start = tk.Button(frame_buttons, text="Start", width=8, command=start_timer)
button_start.grid(row=0, column=0, padx=10)

button_quit = tk.Button(frame_buttons, text="Exit", width=8, command=window.quit)
button_quit.grid(row=0, column=1, padx=10)

# Applica il tema autunnale
apply_theme(themes["autumn"])

#----------------------------------------------------------
def on_radio_selection():
    print(f"You selected: {selected_option.get()}")
    apply_theme(themes[f"{selected_option.get()}"])



# Create a StringVar to hold the selected value
selected_option = tk.StringVar()
selected_option.set("Option 1")  # Default value

# Create Radiobuttons
radio1 = tk.Radiobutton(window, text="Autumn", variable=selected_option, value="autumn")
radio2 = tk.Radiobutton(window, text="Winter", variable=selected_option, value="winter")
radio3 = tk.Radiobutton(window, text="Spring", variable=selected_option, value="spring")
radio4 = tk.Radiobutton(window, text="Summer", variable=selected_option, value="summer")


# Place the Radiobuttons in the window
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")
radio4.pack(anchor="w")


# Create a button to print the selected option
select_button = tk.Button(window, text="Select", command=on_radio_selection)
select_button.pack(pady=10)# Avvio del loop principale
window.mainloop()