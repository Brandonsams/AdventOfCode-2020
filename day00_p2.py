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

# adapters = sorted(input_list)
# adapters = [0] + adapters + [max(adapters) + 3]
dp = [0] * len(jolts)
dp[0] = 1  # Start at the outlet

for i in range(len(jolts)):
    for j in range(i + 1, len(jolts)):
        if jolts[j] - jolts[i] <= 3:
            dp[j] += dp[i]
        else:
            break

print(dp[-1])