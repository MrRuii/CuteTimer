import tkinter as tk
#Funzione per nascondere il pulsante
def hideButton(button: tk.Button | tk.Frame | tk.Label): 
    button.grid_remove()

# Funzione per avviare il pulsante
def startButton(button: tk.Button):
    button.grid()