#filename = "example.txt"
filename = "input.txt"

f = open(filename, "r")

lines = [line.rstrip("\n") for line in f]

ranges = []
ids = []

indexOfEmpty = lines.index('')
for l in range(0,indexOfEmpty):
    ranges.append(lines[l])
for i in range(indexOfEmpty+1,len(lines)):
    ids.append(lines[i])

validIds = []

for id_str in ids:
    id_num = int(id_str)
    for r in ranges:
        floor, roof = map(int, r.split('-'))
        if floor <= id_num <= roof:
            validIds.append(id_num)
            break
print(len(validIds))
