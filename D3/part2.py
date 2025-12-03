#filename = "example.txt"
filename = "input.txt"

total = 0

f = open(filename, "r")
lines = f.readlines()

for line in lines:
    line = line.strip()
    nums = [int(c) for c in line]
    
    chosen = []
    remaining = 12
    start = 0
    while remaining > 0:
        end = len(nums) - remaining + 1
        max_digit = max(nums[start:end])
        idx = nums.index(max_digit, start, end)
        chosen.append(str(max_digit))
        start = idx + 1
        remaining -= 1

    joltage = int("".join(chosen))
    total += joltage

print(total)
