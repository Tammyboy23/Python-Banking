class Account:
    def __init__(self, total):
        self.total = total

    def Add_Expesne(self, amount):
        self.total += amount
        print(f"You have added {amount} Successfully to your total ✅")

    def show_Expense(self):
        print(f"You have spent ${self.total} in total")

account1 = Account(0)
ans = int(input("**** Welcome User ****\n 1. Show total Expenses \n 2.Add Expense \n : "))
match ans:
    case 1:
        account1.show_Expense()
    case 2:
        cash = int(input("How much do you want to Add: "))
        account1.Add_Expesne(cash)
