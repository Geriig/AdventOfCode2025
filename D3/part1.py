#filename = "example.txt"
filename = "input.txt"

f = open(filename, "r")

lines = f.readlines()
osszeg = 0
for line in lines:
    line = line.rstrip()
    firstD = max(line)
    secondD=1
    indexOfMaxim = line.index(firstD)
    
    if(indexOfMaxim == len(line)-1):
        firstD = 1
        secondD = max(line)
        for n in range(0, len(line)-1):
            current = int(line[n])
            if firstD < current:
                firstD = current
    else:
        for n in range(indexOfMaxim+1, len(line)):
            current = int(line[n])
            if secondD < current:
                secondD = current
    osszeg += (int(firstD)*10+int(secondD))

print(osszeg)
