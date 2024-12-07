import re 

name = input("Siapa namamu ? ").strip()

if matches := re.search(r"^(.+),(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hallo {name}")