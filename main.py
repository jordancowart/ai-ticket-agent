ticket = input("Describe the support issue: ")

if "payroll" in ticket.lower():
    category = "Payroll"
elif "time" in ticket.lower():
    category = "Timekeeping"
elif "mobile" in ticket.lower():
    category = "Mobile Access"
else:
    category = "General Support"

print(f"\nSuggested Category: {category}")