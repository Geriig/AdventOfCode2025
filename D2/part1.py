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
        firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]
        if firstpart == secondpart:
            invalidSum+=number

print(invalidSum)


        