fname = "day03_input.txt"
# fname = "day03_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines
lines = load_input(fname=fname)

answer = 1

trees = 0
x = 0
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + 1) % len(line)
answer *= trees

trees = 0
x = 0
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + 3) % len(line)
answer *= trees

trees = 0
x = 0
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + 5) % len(line)
answer *= trees

trees = 0
x = 0
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + 7) % len(line)    
answer *= trees

trees = 0
x = 0
skip = False
for line in lines:
    if skip:
        skip = False
        continue
    skip = True
    if line[x] == "#":
        trees += 1
    x = (x + 1) % len(line)
answer *= trees

print(answer)