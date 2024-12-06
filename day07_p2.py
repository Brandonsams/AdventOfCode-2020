
fname = "day07_input.txt"
# fname = "day07_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

from collections import defaultdict

# Parse the rules into a graph with counts
def parse_rules_with_counts(rules):
    contains = {}
    for rule in rules:
        outer, inner = rule.split(" bags contain ")
        inner_rules = {}
        if "no other bags" not in inner:
            for bag in inner.split(", "):
                count, color = bag.split(" ", 1)
                color = " ".join(color.split(" ")[:2])  # Get the color name
                inner_rules[color] = int(count)
        contains[outer] = inner_rules
    return contains

# Recursive function to compute total bags inside a given bag
def count_bags_inside(graph, bag):
    if not graph[bag]:  # Base case: no other bags
        return 0
    total = 0
    for inner_bag, count in graph[bag].items():
        total += count + count * count_bags_inside(graph, inner_bag)
    return total

# # Input rules
# rules = [
#     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#     "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#     "bright white bags contain 1 shiny gold bag.",
#     "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#     "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#     "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#     "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#     "faded blue bags contain no other bags.",
#     "dotted black bags contain no other bags.",
# ]
rules = load_input(fname=fname)


# Process and solve
graph = parse_rules_with_counts(rules)
result = count_bags_inside(graph, "shiny gold")
print(result)
