import re


fname = "day04_input.txt"
# fname = "day04_input_example.txt"


def is_valid_hex_code(s):
    # Regular expression for a '#' followed by exactly six characters 0-9 or a-f
    pattern = r"^#[0-9a-f]{6}$"
    return bool(re.match(pattern, s))


def is_nine_digit_string(s):
    # Regular expression for a '#' followed by exactly six characters 0-9 or a-f
    pattern = r"^[0-9]{9}$"
    return bool(re.match(pattern, s))


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
    present_required_valid_fields = []

    passport_data = passport.replace("\n", " ")
    for field in passport_data.split():
        field_name, field_value = field.split(":")
        match field_name:
            case "byr":
                if int(field_value) >= 1920 and int(field_value) <= 2002:
                    present_required_valid_fields.append(field_name)
            case "iyr":
                if int(field_value) >= 2010 and int(field_value) <= 2020:
                    present_required_valid_fields.append(field_name)
            case "eyr":
                if int(field_value) >= 2020 and int(field_value) <= 2030:
                    present_required_valid_fields.append(field_name)
            case "hgt":
                if field_value.endswith("cm") and field_value[:-2].isdigit():
                    if int(field_value[:-2]) >= 150 and int(field_value[:-2]) <= 193:
                        present_required_valid_fields.append(field_name)
                elif field_value.endswith("in") and field_value[:-2].isdigit():
                    if int(field_value[:-2]) >= 59 and int(field_value[:-2]) <= 76:
                        present_required_valid_fields.append(field_name)
            case "hcl":
                if is_valid_hex_code(field_value):
                    present_required_valid_fields.append(field_name)
            case "ecl":
                if field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    present_required_valid_fields.append(field_name)
            case "pid":
                if is_nine_digit_string(field_value):
                    present_required_valid_fields.append(field_name)
            case _:
                pass


    if len(present_required_valid_fields) == 7:
        answer += 1


print(answer)
