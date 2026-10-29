
# Hospital Ward Occupancy Monitoring
wards = [
    [8, 10, 12],   # Ward 1
    [15, 18, 20], # Ward 2
    [5, 7, 9]     # Ward 3
]

# Total bed capacity of each ward
capacity = [10, 15, 18]

peak_occupancy = 0
peak_ward = 0
peak_day = 0

for i in range(len(wards)):
    print("\nWard", i + 1)

    for j in range(len(wards[i])):
        occupied = wards[i][j]

        # Calculate utilization percentage
        utilization = (occupied / capacity[i]) * 100

        print("Day", j + 1)
        print("Occupied beds:", occupied)
        print("Utilization:", round(utilization, 2), "%")

        # Detect capacity violations
        if occupied > capacity[i]:
            print("Warning: Capacity exceeded!")
        else:
            print("Capacity is within limit.")

        # Find peak-demand period
        if occupied > peak_occupancy:
            peak_occupancy = occupied
            peak_ward = i + 1
            peak_day = j + 1

print("\n--- Peak Demand Report ---")
print("Highest occupied beds:", peak_occupancy)
print("Peak ward: Ward", peak_ward)
print("Peak day: Day", peak_day)
