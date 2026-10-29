
# University Scholarship Allocation

students = [
    ["Ravi", 85, [80, 85, 90], 90, 150000],
    ["Sita", 90, [90, 88, 92], 95, 120000],
    ["Raju", 90, [85, 90, 90], 90, 100000],
    ["Priya", 70, [65, 75, 70], 80, 200000],
    ["Kiran", 88, [90, 85, 88], 85, 300000]
]

# Scholarship eligibility criteria
min_aggregate = 75
min_subject_marks = 60
min_attendance = 75
max_income = 200000

eligible_students = []

for student in students:
    name = student[0]
    aggregate = student[1]
    subject_marks = student[2]
    attendance = student[3]
    income = student[4]

    # Check subject-wise minimum marks
    subjects_passed = True

    for marks in subject_marks:
        if marks < min_subject_marks:
            subjects_passed = False

    # Check all eligibility conditions
    if (aggregate >= min_aggregate and
        subjects_passed and
        attendance >= min_attendance and
        income <= max_income):

        eligible_students.append(student)
eligible_students.sort(
    key=lambda s: (-s[1], -s[3], s[4])
)

# Display results
print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("---------------------------------")

if len(eligible_students) == 0:
    print("No students are eligible.")
else:
    print("Eligible Students Ranked by Merit:\n")

    for rank, student in enumerate(eligible_students, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Subject Marks:", student[2])
        print("Attendance:", student[3], "%")
        print("Family Income: Rs.", student[4])
        print()
