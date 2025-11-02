# percentage_calculator.py

def calculate_percentage(obtained, total):
    """
    Calculate percentage given obtained and total marks.
    """
    if total == 0:
        return "Total marks cannot be zero!"
    percentage = (obtained / total) * 100
    return f"Percentage: {percentage:.2f}%"

if __name__ == "__main__":
    print("=== Percentage Calculator ===")
    obtained = float(input("Enter obtained marks: "))
    total = float(input("Enter total marks: "))
    print(calculate_percentage(obtained, total))
