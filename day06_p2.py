
fname = "day06_input.txt"
# fname = "day06_input_example.txt"

def load_input(fname):
    rv = ""
    with open(fname) as file:
        rv = file.read()
    return rv

input_data = load_input(fname=fname)

answer = 0
for group in input_data.split("\n\n"):
    forms = []
    for form in group.split("\n"):
        forms.append(set(form))
    
    intersection = set.intersection(*forms)
    answer += len(intersection)


print(answer)