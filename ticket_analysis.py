import csv

issue_counts = {}

recommendations = {
    "Payroll": {
        "priority": "High",
        "recommendation": "Add more payroll deduction, tax, overtime, and direct deposit scenarios to the Platinum database."
    },
    "Timekeeping": {
        "priority": "High",
        "recommendation": "Add stronger mobile clock-in, missing punch, timesheet, and schedule visibility examples to the Platinum database."
    },
    "PTO": {
        "priority": "Medium",
        "recommendation": "Improve PTO balance, manager approval, and request workflow examples."
    },
    "Access": {
        "priority": "Medium",
        "recommendation": "Add clearer login, password reset, account lockout, and access permission scenarios."
    },
    "Scheduling": {
        "priority": "Low",
        "recommendation": "Add basic shift swap and schedule-change examples if this becomes a recurring issue."
    }
}

with open("fake_zendesk_tickets.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        category = row["category"]

        if category in issue_counts:
            issue_counts[category] += 1
        else:
            issue_counts[category] = 1

print("\nTicket Category Analysis")
print("------------------------")

for category, count in issue_counts.items():
    print(f"{category}: {count} tickets")

print("\nPrioritized Platinum DB Recommendations")
print("---------------------------------------")

for category, count in sorted(issue_counts.items(), key=lambda item: item[1], reverse=True):
    priority = recommendations[category]["priority"]
    recommendation = recommendations[category]["recommendation"]

    print(f"\n{priority.upper()} PRIORITY: {category}")
    print(f"Ticket Volume: {count}")
    print(f"Recommended Update: {recommendation}")