#filename = "example.txt"
filename = "input.txt"

with open(filename) as f:
    lines = [line.rstrip("\n") for line in f]

height = len(lines)
width = len(lines[0])

problems = []
current_cols = []

for col in range(width):
    column_chars = [lines[row][col] for row in range(height)]
    if all(ch == ' ' for ch in column_chars):
        if current_cols:
            problems.append(current_cols)
            current_cols = []
    else:
        current_cols.append(column_chars)

if current_cols:
    problems.append(current_cols)

total = 0

for block in problems:
    rows = [''.join(col[row] for col in block) for row in range(height)]

    *numbers, op = rows
    cleaned_numbers = [int(s.strip()) for s in numbers]

    if op.strip() == '+':
        total += sum(cleaned_numbers)
    else:
        product = 1
        for x in cleaned_numbers:
            product *= x
        total += product

print(total)
