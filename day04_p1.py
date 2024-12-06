fname = "day04_input.txt"
# fname = "day04_input_example.txt"


def load_input(fname):
    rv = ""
    with open(fname) as file:
        rv = file.read()
    return rv


input_data = load_input(fname=fname)

answer = 0

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
    # ,"cid"
]

for passport in input_data.split("\n\n"):
    present_required_fields = []

    passport_data = passport.replace("\n", " ")
    for field in passport_data.split():
        field_name = field.split(":")[0]
        if field_name in required_fields:
            present_required_fields.append(field_name)
    if len(present_required_fields) == 7:
        answer += 1


print(answer)
