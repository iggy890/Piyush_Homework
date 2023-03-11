from tkinter import Tk, Label, Entry, Button

class BankAccount:
    def __init__(self, name: str, card_number: int):
        self.name = name
        self.card_number = card_number

window = Tk()
window.title("Bank")
window.geometry("500x200")

# Name entering
describer_name = Label(window, text="Enter Name:")
describer_name.grid(row=1, column=0)

name = Entry(window, width=20)
name.grid(row=2, column=0)

describer_card_number = Label(window, text="Enter Card number:")
describer_card_number.grid(row=1, column=1)

card_number = Entry(window, width=20)
card_number.grid(row=2, column=1)

def create_account():
    name_entry = name.get()
    card_number_entry = int(card_number.get())

    print(name_entry)
    print(card_number_entry)

    account = BankAccount(name_entry, card_number_entry)

create_account_button = Button(window, text="Create Account", command=create_account)
create_account_button.grid(row=2, column=2)

options_label = Label(window, text="Options:")
options_label.grid(row=3, column=1)

window.mainloop()
