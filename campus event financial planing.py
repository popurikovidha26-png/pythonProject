# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))

participants = int(input("Enter number of participants: "))
contribution = float(input("Enter contribution per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate total cost
fixed_cost = venue + equipment + transport
variable_cost = participants * (catering + certificate)
total_cost = fixed_cost + variable_cost

# Calculate total funds
participant_funds = participants * contribution
total_funds = participant_funds + sponsorship

# Calculate shortfall
shortfall = max(0, total_cost - total_funds)

# Minimum registrations to break even
balance_per_person = contribution - catering - certificate

if balance_per_person > 0:
    minimum = max(0, int((fixed_cost - sponsorship) / balance_per_person))
    if minimum * balance_per_person < fixed_cost - sponsorship:
        minimum += 1
    print("Minimum registrations to break even:", minimum)
else:
    print("Break-even is not possible with the given contribution.")

print("Fixed Cost:", fixed_cost)
print("Variable Cost:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", participant_funds)
print("Sponsorship:", sponsorship)
print("Sponsorship/Funding Shortfall:", shortfall)
