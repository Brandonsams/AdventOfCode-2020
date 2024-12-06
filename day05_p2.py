
fname = "day05_input.txt"
# fname = "day05_input_example.txt"


def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


lines = load_input(fname=fname)

seat_ids = []
for line in lines:
    fb = line[:7]
    lr = line[7:]
    fb_bin = fb.replace("B", "1").replace("F", "0")
    lr_bin = lr.replace("R", "1").replace("L", "0")
    # print(int(fb_bin, base=2), int(lr_bin, base=2))
    seat_id = 8*int(fb_bin, base=2) + int(lr_bin, base=2)
    seat_ids.append(seat_id)

seat_ids.sort()

for i,j in zip(seat_ids[:-1],seat_ids[1:]):
    if j-i == 2:
        print(i,j,j-1)

# print(int("101", base=2))
