import re

url = input("URL : ").strip()

username = re.search(r"https://twitter.com/(.+)", url)

if username:
    username = username.group(1) 
    print(f"Username : {username}")
else:
    print("URL tidak valid.")
