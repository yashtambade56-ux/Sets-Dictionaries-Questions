# Count how many unique values exist across dictionary items.

my_dict = {}
for i in range(5):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value

unique_values_count = len(set(my_dict.values()))
print("Number of unique values:", unique_values_count)