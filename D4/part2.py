#filename = "example.txt"
filename = "input.txt"

f=  open(filename, "r")
lines = [list(line.rstrip("\n")) for line in f]

rows = len(lines)
cols = len(lines[0])

dirs = [
    (-1,-1),(-1,0),(-1,1),
    (0,-1),        (0,1),
    (1,-1),(1,0),(1,1)
]

total_removed = 0

while True:
    removable = []

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '@':
                db = 0
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if lines[nr][nc] == '@':
                            db += 1
                if db < 4:
                    removable.append((r, c))

    if not removable:
        break

    for r, c in removable:
        lines[r][c] = '.'
        total_removed += 1

print(total_removed)
