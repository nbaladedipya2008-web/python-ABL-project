
# Progressive Electricity Billing

# Electricity consumption in units for 4 months
months = ["January", "February", "March", "April"]
units = [100, 150, 180, 300]

fixed_charge = 50
surcharge_rate = 5
rebate_rate = 10

bills = []

for i in range(len(units)):
    u = units[i]

    # Calculate charges using progressive slabs
    if u <= 100:
        energy_charge = u * 2
    elif u <= 200:
        energy_charge = 100 * 2 + (u - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (u - 200) * 5

    # Calculate surcharge
    surcharge = energy_charge * surcharge_rate / 100

    # Calculate rebate for consumption up to 100 units
    if u <= 100:
        rebate = energy_charge * rebate_rate / 100
    else:
        rebate = 0

    # Calculate final bill
    total_bill = energy_charge + fixed_charge + surcharge - rebate
    bills.append(total_bill)

    print("\nMonth:", months[i])
    print("Units consumed:", u)
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total bill: Rs.", round(total_bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(1, len(bills)):
    increase = bills[i] - bills[i - 1]

    print(months[i - 1], "to", months[i])
    print("Bill increase: Rs.", round(increase, 2))

    # Identify unusual increases above 50%
    if increase > bills[i - 1] * 0.50:
        print("Warning: Unusual bill increase detected!")
    else:
        print("Bill increase is within normal range.")

# Identify highest bill
highest_bill = max(bills)
highest_month = months[bills.index(highest_bill)]

print("\n--- Highest Bill Report ---")
print("Month:", highest_month)
print("Highest bill: Rs.", round(highest_bill, 2))
