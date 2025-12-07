#filename = "example.txt"
filename = "input.txt"

with open(filename, "r") as f:
    lines = [line.rstrip("\n") for line in f if line.rstrip("\n") != ""]

if not lines:
    print(0)
    raise SystemExit

height = len(lines)
width = max(len(r) for r in lines)
lines = [r.ljust(width) for r in lines]

blocks = []
current = []
for col in range(width):
    col_chars = [lines[row][col] for row in range(height)]
    if all(ch == " " for ch in col_chars):
        if current:
            blocks.append(current)
            current = []
    else:
        current.append(col)
if current:
    blocks.append(current)

grand_total = 0

for block in blocks:
    op = None
    for c in block:
        if lines[-1][c] in "+*":
            op = lines[-1][c]
            break
    if op is None:
        raise ValueError("Operator not found in block; input may be malformed.")

    numbers = []
    for c in reversed(block):
        digit_str = "".join(lines[r][c] for r in range(height - 1)).strip()
        if digit_str == "":
            continue
        numbers.append(int(digit_str))

    if not numbers:
        continue

    if op == "+":
        grand_total += sum(numbers)
    else: 
        prod = 1
        for n in numbers:
            prod *= n
        grand_total += prod

print(grand_total)
