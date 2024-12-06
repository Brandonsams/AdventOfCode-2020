
fname = "day08_input.txt"
# fname = "day08_input_example.txt"


def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


boot_code_input = load_input(fname=fname)

# attempt to change each line in boot code until it terminates
for b in range(len(boot_code_input)):
    if boot_code_input[b].startswith("acc"):
        continue
    boot_code = boot_code_input.copy()
    if boot_code_input[b].startswith("jmp"):
        boot_code[b] = boot_code_input[b].replace("jmp", "nop")
    elif boot_code_input[b].startswith("nop"):
        boot_code[b] = boot_code_input[b].replace("nop", "jmp")
    else:
        continue

    visited_indices = []
    accumulator = 0
    index = 0

    while index not in visited_indices:
        visited_indices.append(index)
        if index == len(boot_code):
            break
        instruction = boot_code[index]
        operation, argument = instruction.split()
        argument_int = int(argument.replace("+", ""))
        match operation:
            case "acc":
                accumulator += argument_int
                index += 1
            case "jmp":
                index += argument_int
            case "nop":
                index += 1

    if index == len(boot_code):
        break

print(accumulator)
