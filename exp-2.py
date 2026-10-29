courses = [
    ("Python", "9-10", "Room1"),
    ("Maths", "10-11", "Room2"),
    ("English", "9-10", "Room1")
]

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1, t1, r1 = courses[i]
        c2, t2, r2 = courses[j]

        if t1 == t2:
            print(c1, "and", c2, "have a time conflict")

        if r1 == r2 and t1 == t2:
            print(r1, "is unavailable")

print("Timetable validation completed")

