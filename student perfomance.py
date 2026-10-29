subjects = ["Maths", "Python", "Physics"]
exam1 = []
exam2 = []

for s in subjects:
    exam1.append(int(input("Enter " + s + " marks in Exam 1: ")))

for s in subjects:
    exam2.append(int(input("Enter " + s + " marks in Exam 2: ")))

print("\nPerformance Analysis")

for i in range(len(subjects)):
    change = exam2[i] - exam1[i]
    print(subjects[i], "Improvement/Decline:", change)

    if exam1[i] < 40 and exam2[i] < 40:
        print("Consistently weak subject")

avg = sum(exam2) / len(subjects)
print("Average Marks:", avg)

if avg >= 75:
    print("Classification: Excellent")
elif avg >= 60:
    print("Classification: Good")
elif avg >= 40:
    print("Classification: Average")
else:
    print("Classification: Poor")
