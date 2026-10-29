# Student Email and Identifier Validation

email = input("Enter student email: ")
reg_id = input("Enter registration identifier: ")

# Validate Email
if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Email format: Valid")
else:
    print("Email format: Invalid")

# Validate Registration Identifier
# Example format: CSE2026001

if len(reg_id) == 10 and reg_id[:3].isalpha() and reg_id[3:9].isdigit() and reg_id[9].isdigit():
    print("Registration Identifier: Valid")
else:
    print("Registration Identifier: Invalid")
