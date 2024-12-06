
fname = "day08_input.txt"
fname = "day08_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

boot_code = load_input(fname=fname)

visited_indices = []
accumulator = 0
index = 0

while index not in visited_indices:
    visited_indices.append(index)
    instruction = boot_code[index]
    operation, argument = instruction.split()
    argument_int = int(argument.replace("+",""))
    match operation:
        case "acc":
            accumulator += argument_int
            index += 1
        case "jmp":
            index += argument_int
        case "nop":
            index += 1

print(accumulator)