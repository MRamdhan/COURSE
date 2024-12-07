import re

email = input("Masukan email : ").strip()

if re.search(r"^(\w|\s)+@+(\w|\s)+\.edu$", email, re.IGNORECASE):
    print(f"Valid \nHallo {email}")
else:
    print("Invalid")