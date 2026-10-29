subjects = int(input("Enter number of subjects: "))
marks = []
grace = 5
maximum = 100

for i in range(subjects):
    m = int(input("Enter subject marks: "))
    if m < 0 or m > maximum:
        print("Invalid marks!")
        exit()
    marks.append(m)

# Apply grace marks
for i in range(subjects):
    if marks[i] < 35 and marks[i] + grace >= 35:
        marks[i] = min(marks[i] + grace, maximum)

print("Final Marks:", marks)

if min(marks) >= 35:
    percentage = sum(marks) / subjects
    print("Percentage:", percentage)

    if percentage >= 75:
        print("Result: Distinction")
    elif percentage >= 60:
        print("Result: First Class")
    elif percentage >= 50:
        print("Result: Second Class")
    else:
        print("Result: Pass")
else:
    print("Result: Fail")
