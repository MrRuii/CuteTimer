themes = {
    "autumn": {
        "bg": "#f5deb3",              # Sfondo beige chiaro (colore di sfondo principale)
        "fg_title": "#8B4513",        # Colore marrone scuro per il testo del titolo
        "fg_label": "#8B4513",        # Colore marrone scuro per il testo delle etichette
        "fg_timer": "#ff8c00",        # Colore arancione scuro per il timer
        "entry_bg": "#ffe4b5",        # Colore beige chiaro per il campo di input
        "entry_fg": "#8B4513",        # Colore marrone scuro per il testo nei campi di input
        "button_start_bg": "#32cd32", # Verde per il pulsante Start
        "button_start_fg": "white",   # Bianco per il testo del pulsante Start
        "button_quit_bg": "#ff4500",  # Arancione scuro per il pulsante Exit
        "button_quit_fg": "white",    # Bianco per il testo del pulsante Exit
        "font_title": ("Arial", 24, "bold"),  # Font del titolo
        "font_label": ("Arial", 14),          # Font delle etichette
        "font_timer": ("Arial", 48, "bold"),  # Font del timer
        "font_button": ("Arial", 12, "bold")  # Font dei pulsanti
    }
}

# # Stile
# title_font = ("Comic Sans MS", 24, "bold")
# label_font = ("Arial", 14)
# button_font = ("Arial", 14, "bold")


# # Etichetta del titolo
# label_title = tk.Label(window, text=" 🍂 Cute Timer 🍂", font=title_font, fg="#8B4513", bg="#f5deb3")
# label_title.pack(pady=5)

# # Etichette e campi di input
# frame_input = tk.Frame(window, bg="#f5deb3")
# frame_input.pack()

# label_minutes = tk.Label(frame_input, text="Minutes:", font=label_font, bg="#f5deb3", fg="#8B4513")
# label_minutes.grid(row=0, column=0, padx=5)
# entry_minutes = tk.Entry(frame_input, width=5, font=label_font, bg="#f5deb3")
# entry_minutes.grid(row=0, column=1, padx=5)

# label_seconds = tk.Label(frame_input, text="Seconds:", font=label_font, bg="#f5deb3", fg="#8B4513")
# label_seconds.grid(row=0, column=2, padx=5)
# entry_seconds = tk.Entry(frame_input, width=5, font=label_font, bg="#f5deb3")
# entry_seconds.grid(row=0, column=3, padx=5)

# # Etichetta per il timer
# label_timer = tk.Label(window, text="00:00", font=("Arial", 48, "bold"), fg="#ff8c00", bg="#f5deb3")
# label_timer.pack()

# # Pulsanti
# frame_buttons = tk.Frame(window, bg="#f5deb3")
# frame_buttons.pack(pady=1)

# button_start = tk.Button(frame_buttons, text="Start", font=button_font, bg="#32cd32", fg="white", command=start_timer)
# button_start.grid(row=0, column=0, padx=5, pady=5)

# button_quit = tk.Button(frame_buttons, text="Exit", font=button_font, bg="#ff4500", fg="white", command=window.quit)
# button_quit.grid(row=0, column=1, padx=5, pady=5)
