with open("input.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
last_three_lines = lines[-3:]

print("Total number of lines:", line_count)
print("Last three lines:")
for line in last_three_lines:
    print(line.strip())

with open("output.txt", "w") as file:
    file.writelines(last_three_lines)

print("\nLast three lines have been written to output.txt")