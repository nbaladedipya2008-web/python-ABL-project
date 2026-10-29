# Smart Parking Fee Management

vehicle = input("Enter vehicle type (Bike/Car/Truck): ").title()
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    from datetime import datetime, timedelta

    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if vehicle not in ["Bike", "Car", "Truck"]:
        print("Invalid vehicle type!")

    else:
        if end < start:
            end += timedelta(days=1)

        minutes = int((end - start).total_seconds() / 60)

        if minutes == 0:
            print("Invalid parking duration!")
        else:
            hours = (minutes + 59) // 60

            rates = {"Bike": 10, "Car": 20, "Truck": 30}
            fee = hours * rates[vehicle]

            # Overnight parking charge
            if end.date() > start.date():
                fee += 50

            # Daily limit
            fee = min(fee, 300)

            # Penalty for parking over 24 hours
            if minutes > 1440:
                fee += 100

            print("Parking duration:", hours, "hours")
            print("Total parking fee: Rs.", fee)

except ValueError:
    print("Invalid time! Enter time in HH:MM format.")