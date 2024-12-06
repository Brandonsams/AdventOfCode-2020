fname = "day03_input.txt"
fname = "day03_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

answer = 0
x = 0
lines = load_input(fname=fname)
for line in lines:
    if line[x] == "#":
        answer += 1
    x = (x + 3) % len(line)

print(answer)