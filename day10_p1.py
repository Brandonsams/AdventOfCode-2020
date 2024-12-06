import itertools

fname = "day10_input.txt"
# fname = "day10_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

input_data = sorted(list(map(int,load_input(fname=fname))))
jolts = [0] + input_data + [max(input_data) + 3]

diffs = []
for a,b in zip(jolts[0::],jolts[1::]):
    diffs.append(b-a)

print(diffs.count(1) * diffs.count(3))