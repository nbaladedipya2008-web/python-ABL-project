# Railway Fare and Reservation Calculator

passengers = [
    ("Ravi", 100, "Sleeper", 20, "No"),
    ("Sita", 250, "AC", 65, "No"),
    ("Arun", 400, "Sleeper", 10, "Yes")
]

for name, distance, cls, age, cancel in passengers:

    # Distance-based fare
    if distance <= 100:
        fare = distance * 1
    elif distance <= 300:
        fare = 100 + (distance - 100) * 1.5
    else:
        fare = 400 + (distance - 300) * 2

    if cls == "AC":
        fare *= 2

    # Age concession
    if age >= 60:
        fare *= 0.60
    elif age <= 12:
        fare *= 0.50

    # Reservation fee
    fee = 50 if cls == "AC" else 20
    total = fare + fee

    print("\nPassenger:", name)

    if cancel == "Yes":
        penalty = total * 0.25
        print("Refund:", round(total - penalty, 2))
        print("Cancellation penalty:", round(penalty, 2))
    else:
        print("Travel class:", cls)
        print("Total fare: Rs.", round(total, 2))