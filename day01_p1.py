fname = "day01_input.txt"
# fname = "day01_input_example.txt"


def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


lines = load_input(fname=fname)

nums = list(map(int, lines))

target = 2020
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i] * nums[j])
            exit

