import customtkinter
import random


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def update() -> None:
    password = generate_password()
    password_text.configure(text=password)



def slider_event(value: int) -> None:
    options["length"] = int(value)
    update()

def letters_event() -> None:
    options["letters"] = letters_checkbox.get()
    update()

def numbers_event() -> None:
    options["numbers"] = numbers_checkbox.get()
    update()

def symbols_event() -> None:
    options["symbols"] = symbols_checkbox.get()
    update()

root = customtkinter.CTk()
root.geometry("500x750")

def is_clipboard_empty():
    try:
        root.selection_get(selection="CLIPBOARD")
    except:    # error raised when empty
        return True
    return False    

def copy(text: str) -> None:
    if is_clipboard_empty():
        root.clear_clipboard()
    root.clipboard_append(text)

letters = customtkinter.StringVar(value="on")
numbers = customtkinter.StringVar(value="on")
symbols = customtkinter.StringVar(value="on")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, font=('Roboto', 24), text="Password Generator")
title.pack(pady=20, padx=10)



letters_checkbox = customtkinter.CTkCheckBox(master=frame, text="Letters", command=letters_event, variable=letters, onvalue="on", offvalue="off")
letters_checkbox.pack(pady=10, padx=10)

numbers_checkbox = customtkinter.CTkCheckBox(master=frame, text="Numbers", command=numbers_event, variable=numbers, onvalue="on", offvalue="off")
numbers_checkbox.pack(pady=10, padx=10)

symbols_checkbox = customtkinter.CTkCheckBox(master=frame, text="Symbols", command=symbols_event, variable=symbols, onvalue="on", offvalue="off")
symbols_checkbox.pack(pady=10, padx=10)

label = customtkinter.CTkLabel(master=frame, font=('Roboto', 12), text="Password Length")
label.pack(pady=5, padx=10)

lengthSlider = customtkinter.CTkSlider(master=frame, number_of_steps=49, from_=1, to=50, command=slider_event)
lengthSlider.pack(pady=5, padx=10)

password_text = customtkinter.CTkLabel(master=frame, font=('Roboto', 12), text="zfzfs")
password_text.pack(pady=5, padx=10)


copy_button = customtkinter.CTkButton(master=frame, text='Copy', command=lambda: copy(password_text.cget("text")))
copy_button.pack(pady=5, padx=10)

options = {
    "letters": 'on',
    "numbers": 'on',
    "symbols": 'on',
    "length": 5
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = [letter.upper() for letter in letters]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&"]

def generate_password() -> str:
    character_sets = []
    if options.get("letters") == "on":
        character_sets.append(letters)
    if options.get("numbers") == "on":
        character_sets.append(numbers)
    if options.get("symbols") == "on":
        character_sets.append(symbols)

    all_characters = [char for char_set in character_sets for char in char_set]

    password = ""
    for _ in range(options.get("length")):
        password += random.choice(all_characters)
    
    return password

root.mainloop()