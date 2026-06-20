import csv
import re

email_re = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

def validate(email):
    return bool(email_re.match(email))

valid_email = 0
row_count = 0

with open("MOCK_DATA.csv",
    "r", encoding = "utf-8") as f:

    invalid_email = 0

    for index, row in enumerate(csv.DictReader(f),start=2):
        row_count += 1
        email = row.get("email", "")

        if not validate(email):
            invalid_email += 1
            print(f"FAIL: row {index} has an incorrect email format. Invalid email: {email}")
            
        
        else:
            valid_email += 1
        
        
    print("\nValidation Summary:")
    print(f"\nTotal number of invalid email addresses: {invalid_email}")
    print(f"\nTotal number of valid email addresses: {valid_email}")
    print(f"\nTotal rows processed: {row_count}")
