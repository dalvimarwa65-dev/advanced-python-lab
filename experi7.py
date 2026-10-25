import re

filename = "input.txt"

pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

with open(filename, "r") as file:
    text = file.read()

emails = re.findall(pattern, text)

print("Valid email addresses found:")

for email in emails:
    print(email)

print(f"\nTotal email addresses:", len(emails))