class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, destination_category):
        if not self.withdraw(amount, f"Transfer to {destination_category.name}"):
            return False
        destination_category.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        title = f"{self.name:*^30}\n"

        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = "{:.2f}".format(entry["amount"])[:7]
            items += f"{description:<23}{amount:>7}\n"

        total = "{:.2f}".format(self.get_balance())
        output = title + items + f"Total: {total}"
        return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

def create_spend_chart(categories):
    # Calculate total withdrawals (spending) per category
    spent_amounts = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)

    # Percentage spent per category, rounded down to the nearest 10
    percentages = [(spent / total_spent) * 100 // 10 * 10 for spent in spent_amounts]

    # Title
    chart = "Percentage spent by category\n"

    # Y-axis lines from 100 down to 0, step -10
    for value in range(100, -1, -10):
        chart += f"{value:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= value else "   "
        chart += "\n"

    # Horizontal line: two spaces past the last bar
    max_name_length = max(len(category.name) for category in categories)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names, written vertically
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            name = category.name
            chart += f"{name[i]}  " if i < len(name) else "   "
        chart += "\n" if i != max_name_length - 1 else ""

    return chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(33.40, "movies")

print(create_spend_chart([food, entertainment]))