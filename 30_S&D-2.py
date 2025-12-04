# Create a dictionary of 5 students marks and print topper.

marks = {}
for i in range(5):
    name = input(f"Enter name of student {i + 1}: ")
    score = int(input(f"Enter marks of {name}: "))
    marks[name] = score

topper = max(marks, key=marks.get)
print(f"The topper is {topper} with marks {marks[topper]}")