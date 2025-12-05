#filename = "example.txt"
filename = "input.txt"

f = open(filename, "r")
lines = [line.rstrip("\n") for line in f]

ranges = []
indexOfEmpty = lines.index('')
for l in range(indexOfEmpty):
    floor, roof = map(int, lines[l].split('-'))
    ranges.append((floor, roof))

ranges.sort()

merged = []
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)    
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end

merged.append((cur_start, cur_end))

total = sum((end - start + 1) for start, end in merged)

print(total)
