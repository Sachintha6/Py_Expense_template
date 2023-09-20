from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
]


class Expense:
    def __init__(self, amount, spender, label):
        self.amount = amount
        self.label = label
        self.spender = spender  

def new_expense(*args):
    infos = prompt(expense_questions)

    expense = Expense()
    expense.amount = infos['amount']
    expense.label = infos['label']
    expense.spender = infos['spender']
    
    f = open('expense_report.csv', 'a', newline='')
    f.write(str(expense.amount) + "-" + str(expense.spender) + "-" + str(expense.label) + "\n"))
    
    print("Expense Added !")
    return True