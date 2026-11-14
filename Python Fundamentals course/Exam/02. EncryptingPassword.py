import re

count_row = int(input())

pattern = r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$"

for i in range(count_row):
    password = input()
    match = re.match(pattern, password)
    if match:
      encrypted_password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
      print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")