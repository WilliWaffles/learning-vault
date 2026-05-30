# creating the main window
# initializing views
# showing and hiding views
# handling basic navigation between views

from tkinter import *
from tkinter import ttk

# Main window
root = Tk()
root.geometry("1080x900")
root.title("Learning Vault")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Main frame
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Labels en main frame
learning_vault_title_label = ttk.Label(main_frame, text="Learning Vault")
language_selection_subtitle_label = ttk.Label(main_frame, text="Select a language")
# Show labels
learning_vault_title_label.grid(row=0, column=0, sticky="w", pady=10)
language_selection_subtitle_label.grid(row=1, column=0, sticky="w")


# Mainloop
root.mainloop()