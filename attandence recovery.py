# Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
threshold = float(input("Enter eligibility percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")
else:
    percentage = (attended / conducted) * 100
    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= threshold:
        print("You are already eligible.")
    else:
        required = 0
        while ((attended + required) / (conducted + required)) * 100 < threshold:
            required += 1

        print("Minimum consecutive classes required:", required)

        future = int(input("Enter additional classes you may attend: "))
        future_percentage = ((attended + future) / (conducted + future)) * 100
        print("Future Attendance:", round(future_percentage, 2), "%")

        if future_percentage >= threshold:
            print("Eligibility achieved.")
        else:
            print("Eligibility not achieved.")
