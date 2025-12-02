def valid(s):
    L = len(s)
    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        part = s[:k]
        if part * (L // k) == s:
            return True
    return False




#filename = "example.txt"
filename = "input.txt"

f = open(filename, "r")

invalidSum=0

data = f.readline()
idranges = data.split(',')
for i in idranges:
    ids = i.split('-')
    for number in range(int(ids[0]), int(ids[1])+1):
        s = str(number)
        if valid(s):
            invalidSum += number

print(invalidSum)


        