# Food Waste Monitoring System

days = int(input("Enter number of days: "))
limit = float(input("Enter acceptable wastage percentage: "))

for i in range(days):
    print("\nDay", i + 1)
    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid data")
        continue

    leftovers = prepared - served
    wastage = (leftovers / prepared) * 100

    print("Leftover Meals:", leftovers)
    print("Wastage Percentage:", round(wastage, 2), "%")

    if wastage > limit:
        print("Warning: Wastage exceeds acceptable limit")
    else:
        print("Wastage is within the acceptable limit")
