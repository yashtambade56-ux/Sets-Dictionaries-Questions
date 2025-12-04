# Input two sets and print union, intersection, and difference.

set1 = set()
set2 = set()
for i in range(5):
    elem1 = input(f"Enter element {i + 1} for set 1: ")
    set1.add(elem1)
for i in range(5):
    elem2 = input(f"Enter element {i + 1} for set 2: ")
    set2.add(elem2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))