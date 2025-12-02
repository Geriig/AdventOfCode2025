#filename = "example.txt"
#filename = "example2.txt"
filename = "input.txt"

f = open(filename, "r")

volume = 50
zeroes = 0

lines = f.readlines()
for line in lines:
    direction = line[0]
    steps = int(line[1:])
    for i in range(steps):
        if direction == 'L':
            volume -= 1
            if  volume < 0:
                volume = 99
        else:
            volume +=1
            if volume > 99:
                volume=0
        if volume == 0:
            zeroes +=1

print(zeroes)

    