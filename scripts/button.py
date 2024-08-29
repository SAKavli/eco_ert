#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def get_user_input(info_text):
    #Setup of window
    root = tk.Tk()
    root.geometry("800x350")
    root.resizable(False,False)
    root.title("Input to eco.ert")

    #Setup of input variables
    house_price = tk.StringVar()
    equity = tk.StringVar()
    salary = tk.StringVar()
    monthly_expenses = tk.StringVar()

    #Close window when submit button is pressed
    def ok_clicked():
        root.destroy()

    #Input frame
    dialoguebox = ttk.Frame(root)
    dialoguebox.pack(padx=10, pady=10, fill='x', expand=True)
    
    #Info label
    info_label = ttk.Label(dialoguebox, text = info_text)
    info_label.pack(fill="x",expand=True)

    #House price
    house_label = ttk.Label(dialoguebox, text = "What is the price of the house?")
    house_label.pack(fill="x",expand=True)

    house_entry = ttk.Entry(dialoguebox, textvariable=house_price)
    house_entry.pack(fill="x", expand=True)
    house_entry.focus()

    #Equity
    equity_label = ttk.Label(dialoguebox, text = "What is your equity in this purchase?")
    equity_label.pack(fill="x",expand=True)

    equity_entry = ttk.Entry(dialoguebox, textvariable=equity)
    equity_entry.pack(fill="x", expand=True)
    equity_entry.focus()

    #Salary
    salary_label = ttk.Label(dialoguebox, text = "What is your yearly salary? (Brutto)")
    salary_label.pack(fill="x",expand=True)

    salary_entry = ttk.Entry(dialoguebox, textvariable=salary)
    salary_entry.pack(fill="x", expand=True)
    salary_entry.focus()
    
    #Montly expenses
    monthly_expenses_label = ttk.Label(dialoguebox, text = "What is your estimated monthly expenses from groceries, spare time activities/equipment etc.?")
    monthly_expenses_label.pack(fill="x",expand=True)

    monthly_expenses_label = ttk.Entry(dialoguebox, textvariable=monthly_expenses)
    monthly_expenses_label.pack(fill="x", expand=True)
    monthly_expenses_label.focus()

    #OK button
    ok_button = ttk.Button(dialoguebox, text="Simulate my loan", command=ok_clicked)
    ok_button.pack(fill="x", expand=True, pady=10)

    root.mainloop()
    
    #Either if user submits empty imput boxes or exits the window while input boxes are empty,
    #allow the user to exit the window without being prompted again.
    if house_price.get() == "" and equity.get() == "" and salary.get() == "" and monthly_expenses.get() == "":
        exit_workflow()
    
    #Check if input can be converted to integers
    try:
        int(house_price.get())
        int(equity.get())
        int(salary.get())
        int(monthly_expenses.get())
    except ValueError:
        return False #Return False if input cannot be converted to integers

    with open("userinput.txt", "w", encoding="utf-8") as f:
        f.write(f"{house_price.get()} {equity.get()} {salary.get()} {monthly_expenses.get()}")
    return True #Return True if input is accepted

#Create dialogue window informing about exiting input windows with incomplete setup.
def exit_workflow():
    #Setup of window
    root = tk.Tk()
    root.geometry("800x250")
    root.resizable(False,False)
    root.title("Exit workflow setup")
    #Input frame
    dialoguebox = ttk.Frame(root)
    dialoguebox.pack(padx=10, pady=10, fill='x', expand=True)

    #Exit info
    equity_label = ttk.Label(dialoguebox, text = "Workflow exited, setup incomplete")
    equity_label.pack(fill="x",expand=True)
    root.mainloop()
    exit()

input_is_valid = get_user_input("Hi! Please fill in your information to simulate when you will be debt free!\n(Enter empty boxes to exit)\n\n")
while not input_is_valid:  #Keep asking for input until input is valid
    input_is_valid = get_user_input("Sorry, you have entered something invalid, please enter only numbers\n(Enter empty boxes to exit)\n\n")