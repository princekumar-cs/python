# percentage.py
import os

print("=== Percentage Calculator ===")

# Detect if running in GitHub Actions (no input possible)
running_in_actions = os.getenv("GITHUB_ACTIONS") == "true"

if running_in_actions:
    obtained = 85
    total = 100
    print(f"Running in GitHub Actions — using test data: {obtained}/{total}")
else:
    obtained = float(input("Enter obtained marks: "))
    total = float(input("Enter total marks: "))

percentage = (obtained / total) * 100
print(f"Percentage: {percentage:.2f}%")
