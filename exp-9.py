# Multi-Event Sports Scheduling and Scoring

events = [
    ("Football", "09:00", "10:00"),
    ("Basketball", "10:00", "11:00"),
    ("Cricket", "09:30", "10:30")
]

scores = [
    ("Team A", 10),
    ("Team B", 15),
    ("Team C", 12)
]

# Check scheduling conflicts
print("Scheduling Conflicts:")

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        name1, start1, end1 = events[i]
        name2, start2, end2 = events[j]

        if start1 < end2 and start2 < end1:
            print(name1, "and", name2, "have a conflict")

# Display team scores
print("\nTeam Scores:")
for team, points in scores:
    print(team, ":", points, "points")

# Generate final rankings
scores.sort(key=lambda x: x[1], reverse=True)

print("\nFinal Rankings:")
for rank, (team, points) in enumerate(scores, start=1):
    print(rank, team, "-", points, "points")