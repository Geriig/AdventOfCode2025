filename = "example.txt"
#filename = "input.txt"

f = open(filename, "r")

acsessable = 0
lines = [line.rstrip("\n") for line in f]

rows = len(lines)
cols = len(lines[0])

dirs = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),         (0,1),
    (1,-1), (1,0), (1,1)
]

for r in range (rows):
    for c in range(cols):
        if lines[r][c] == '@':
            db = 0
            for d_row, d_col in dirs:
                new_row = r+d_row
                new_col = c+d_col

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if lines[new_row][new_col] == '@':
                        db += 1
            if db < 4:
                acsessable += 1
print (acsessable)


                