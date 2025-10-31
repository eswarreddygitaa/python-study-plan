# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, 
# add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []   
        self.expenses = [] 
    
    def add_income(self, description, amount):
        self.incomes.append((description, amount))
    
    def add_expense(self, description, amount):
        self.expenses.append((description, amount))
    
    def total_income(self):
        return sum(amount for _, amount in self.incomes)
    
    def total_expense(self):
        return sum(amount for _, amount in self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print("\nIncomes:")
        for desc, amt in self.incomes:
            print(f"  - {desc}: +{amt}")
        print(f"Total Income: {self.total_income()}")
        
        print("\nExpenses:")
        for desc, amt in self.expenses:
            print(f"  - {desc}: -{amt}")
        print(f"Total Expense: {self.total_expense()}")
        
        print(f"\nAccount Balance: {self.account_balance()}")


person = PersonAccount('Eswar Reddy', 'Pagadala')

person.add_income('Salary', 50000)
person.add_income('Freelance Project', 15000)

person.add_expense('Rent', 12000)
person.add_expense('Groceries', 5000)
person.add_expense('Internet Bill', 1000)

person.account_info()
