
fname = "day07_input.txt"
# fname = "day07_input_example.txt"

def load_input(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

from collections import defaultdict

# Parse the rules into a graph
def parse_rules(rules):
    contains = defaultdict(list)
    for rule in rules:
        outer, inner = rule.split(" bags contain ")
        if "no other bags" in inner:
            continue
        for bag in inner.split(", "):
            count, color = bag.split(" ", 1)
            color = " ".join(color.split(" ")[:2])  # Get the color name
            contains[color].append(outer)
    return contains

# Perform DFS to find all possible containers
def find_all_containers(graph, start):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])
    return visited

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
graph = parse_rules(rules)
containers = find_all_containers(graph, "shiny gold")
print(len(containers) - 1)  # Subtract 1 to exclude the shiny gold bag itself