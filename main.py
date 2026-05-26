ticket = input("Describe the support issue: ").lower()

result = {
    "category": "General Support",
    "priority": "Low",
    "likely_issue": "The issue needs additional review.",
    "recommended_next_steps": [
        "Gather more details from the user.",
        "Confirm when the issue started.",
        "Check if other users are affected."
    ]
}

if "payroll" in ticket or "paycheck" in ticket or "pay" in ticket:
    result = {
        "category": "Payroll",
        "priority": "High",
        "likely_issue": "The employee may have a payroll configuration, earnings, deduction, or processing issue.",
        "recommended_next_steps": [
            "Confirm the impacted pay period.",
            "Review employee payroll settings.",
            "Check earnings, deductions, and tax setup.",
            "Verify whether the issue affects one employee or multiple employees."
        ]
    }

elif "clock" in ticket or "time" in ticket or "timesheet" in ticket:
    result = {
        "category": "Timekeeping",
        "priority": "Medium",
        "likely_issue": "The employee may have a timesheet, punch, schedule, or access issue.",
        "recommended_next_steps": [
            "Confirm the employee's assigned schedule.",
            "Review recent punches.",
            "Check whether the employee has access to clock in.",
            "Verify manager approval status."
        ]
    }

elif "mobile" in ticket or "app" in ticket or "login" in ticket:
    result = {
        "category": "Mobile Access",
        "priority": "Medium",
        "likely_issue": "The employee may have a login, access profile, or mobile permission issue.",
        "recommended_next_steps": [
            "Confirm the employee can log in from desktop.",
            "Verify mobile access permissions.",
            "Check whether the employee is active.",
            "Confirm the correct username is being used."
        ]
    }

print("\nTicket Triage Result")
print("--------------------")
print(f"Category: {result['category']}")
print(f"Priority: {result['priority']}")
print(f"Likely Issue: {result['likely_issue']}")
print("\nRecommended Next Steps:")

for step in result["recommended_next_steps"]:
    print(f"- {step}")
