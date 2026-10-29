# University Hostel Room Allocation

students = [
    ("Ravi", "Male"),
    ("Sita", "Female"),
    ("Arun", "Male"),
    ("Priya", "Female")
]

rooms = [
    ("Room1", "Male", 2),
    ("Room2", "Female", 2)
]

allocations = []
counts = {}

for room, gender, capacity in rooms:
    counts[room] = 0

    for name, student_gender in students:
        if student_gender == gender and counts[room] < capacity:
            if name not in [a[0] for a in allocations]:
                allocations.append((name, room))
                counts[room] += 1
                print(name, "allocated to", room)

# Check duplicate assignments
print("\nDuplicate Assignment Check:")
names = [a[0] for a in allocations]

if len(names) == len(set(names)):
    print("No duplicate assignments.")
else:
    print("Duplicate assignments found!")

# Display room occupancy
print("\nRoom Occupancy:")
for room, gender, capacity in rooms:
    occupied = counts[room]
    print(room, ":", occupied, "/", capacity)

print("\nTotal students allocated:", len(allocations))
print("Total students unallocated:", len(students) - len(allocations))