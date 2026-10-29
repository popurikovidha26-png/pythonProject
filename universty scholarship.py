marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

percentage = sum(marks) / 5

if min(marks) >= 60 and percentage >= 75 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

print("Percentage:", percentage)
