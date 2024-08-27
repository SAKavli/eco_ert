#!/usr/bin/env python
import json
from time import sleep as sleep

def evaluate(coeffs,debt,salary,monthly_expenses):
    int_rate = coeffs["interest_rate"]
    tax = coeffs["tax"]

    monthly_salary = salary/12 * (1-tax/100)
    monthly_interest = debt*int_rate/1200
    monthly_repay = monthly_salary - monthly_interest - monthly_expenses
    return max(0,(debt - monthly_repay))

def main():
    #Read coeff values
    with open("parameters.json", encoding="utf-8") as f:
        coeffs = json.load(f)["COEFFS"]
    

    #Read user input
    with open("userinput.txt", "r", encoding="utf-8") as f:
        house_price, equity, salary, monthly_expenses = [int(x) for x in f.readline().split()]
    #Initialize debt value
    debt =  house_price - equity
    i = 0
    output = [debt]
    while debt>0:
        debt = evaluate(coeffs,debt,salary,monthly_expenses)
        output.append(debt)
        i += 1
        """
        When there has been 100 realizations and
        the monthly repay is smaller than the
        interest, terminate the simulation
        """
        if i == 100 and output[-2] < output[-1]:
            break

    with open("eco.out", "w", encoding="utf-8") as f:
        f.write("\n".join(map(str,output)))

if __name__ == "__main__":
    main()