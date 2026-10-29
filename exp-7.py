
# Multi-Currency Travel Budget Analysis

expenses = [
    ("Hotel", 200, "USD"),
    ("Food", 100, "EUR"),
    ("Shopping", 150, "USD"),
    ("Transport", 5000, "INR")
]

rates = {"USD": 83, "EUR": 90, "INR": 1}
conversion_fee = 2
budget = 40000

total = 0
category_totals = {}

for category, amount, currency in expenses:
    converted = amount * rates[currency]
    fee = converted * conversion_fee / 100
    final_amount = converted + fee

    category_totals[category] = final_amount
    total += final_amount

    print(category, "Cost in INR:", round(final_amount, 2))

print("\nTotal Travel Cost: Rs.", round(total, 2))
print("Budget: Rs.", budget)

if total > budget:
    print("Warning: Budget exceeded!")
else:
    print("Travel is within budget.")

largest = max(category_totals, key=category_totals.get)
print("Largest Expense:", largest)
print("Amount: Rs.", round(category_totals[largest], 2))
