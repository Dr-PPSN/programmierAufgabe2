import tkinter as tk
from tkinter import messagebox


def show_invoice():
    # Hier kannst du die Logik für die Rechnungserstellung einfügen
    messagebox.showinfo("Rechnung", "Rechnung wird angezeigt")


def submit_booking():
    # Hier kannst du die Logik für die Buchungserstellung einfügen
    messagebox.showinfo("Buchung", "Buchung wurde erstellt")


# Hauptfenster erstellen
root = tk.Tk()
root.title("Buchungsabrechnung")


# Funktion, um die Status der Checkboxen zu aktualisieren
def update_checkboxes():
    if checkbox1_var.get() == 1:
        checkbox2_var.set(0)
    if checkbox2_var.get() == 1:
        checkbox1_var.set(0)


# Checkboxen
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

checkbox1_var = tk.IntVar()
checkbox1_var.set(1)
checkbox1 = tk.Checkbutton(checkbox_frame, text="Checkbox 1", variable=checkbox1_var, command=update_checkboxes)
checkbox1.grid(row=0, column=0, sticky="w")

checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(checkbox_frame, text="Checkbox 2", variable=checkbox2_var, command=update_checkboxes)
checkbox2.grid(row=0, column=1, sticky="w")

# Eingabefelder
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Art:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
art_entry = tk.Entry(input_frame)
art_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Von:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
von_entry = tk.Entry(input_frame)
von_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Bis:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
bis_entry = tk.Entry(input_frame)
bis_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Preis in Euro:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
preis_entry = tk.Entry(input_frame)
preis_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

submit_button = tk.Button(button_frame, text="Buchung erstellen", command=submit_booking)
submit_button.grid(row=0, column=0, padx=5)

invoice_button = tk.Button(button_frame, text="Rechnung anzeigen", command=show_invoice)
invoice_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Beenden", command=root.quit)
exit_button.grid(row=0, column=2, padx=5)

root.mainloop()
