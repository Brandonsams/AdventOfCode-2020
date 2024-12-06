import itertools

fname = "day09_input.txt"
# fname = "day09_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

preamble_length = 25
if fname == "day09_input_example.txt":
    preamble_length = 5

data = list(map(int,load_input(fname=fname)))

for index in range(preamble_length,len(data)):
    slice = data[index-preamble_length:index]
    sum_found = False
    for a,b in itertools.permutations(slice,r=2):
        if a+b == data[index]:
            sum_found = True
            break
    if not sum_found:
        break

print(data[index])