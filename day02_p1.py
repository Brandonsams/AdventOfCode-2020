fname = "day02_input.txt"
# fname = "day02_input_example.txt"


def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def is_valid_password(line):
    count, char, password = line.replace(":", "").split(" ")
    count_min, count_max = map(int, count.split("-"))
    return password.count(char) >= count_min and password.count(char) <= count_max


lines = load_input(fname=fname)

answer = 0
for line in lines:
    if is_valid_password(line):
        answer += 1

print(answer)
