
# Student Performance Trend Analysis
name = input("Enter student name: ")

subjects = ["Python", "Maths", "English"]

exam1 = []
exam2 = []
exam3 = []

# Input marks for three examinations
for subject in subjects:
    print("\nEnter marks for", subject)
    m1 = float(input("Exam 1 marks: "))
    m2 = float(input("Exam 2 marks: "))
    m3 = float(input("Exam 3 marks: "))

    exam1.append(m1)
    exam2.append(m2)
    exam3.append(m3)

# Calculate total and average marks
total = sum(exam1) + sum(exam2) + sum(exam3)
average = total / 9

print("\n--- Student Performance Report ---")
print("Student Name:", name)

# Compare examination marks
for i in range(len(subjects)):
    improvement = exam3[i] - exam1[i]

    print("\nSubject:", subjects[i])
    print("Exam 1:", exam1[i])
    print("Exam 2:", exam2[i])
    print("Exam 3:", exam3[i])

    if improvement > 0:
        print("Performance: Improved by", improvement, "marks")
    elif improvement < 0:
        print("Performance: Declined by", abs(improvement), "marks")
    else:
        print("Performance: No change")

# Identify consistently weak subjects
print("\n--- Weak Subjects ---")
weak_found = False

for i in range(len(subjects)):
    if exam1[i] < 40 and exam2[i] < 40 and exam3[i] < 40:
        print(subjects[i], "is consistently weak")
        weak_found = True

if not weak_found:
    print("No consistently weak subjects")

# Classify the student
print("\nAverage Marks:", round(average, 2))

if average >= 80:
    print("Classification: Excellent")
elif average >= 60:
    print("Classification: Good")
elif average >= 40:
    print("Classification: Average")
else:
    print("Classification: Needs Improvement")
