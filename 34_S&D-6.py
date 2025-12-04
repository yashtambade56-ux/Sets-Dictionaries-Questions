# Reverse a dictionary (swap keys & values).

original_dict = {}
for i in range(5):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    original_dict[key] = value

reversed_dict = {value: key for key, value in original_dict.items()}
print("Reversed dictionary:", reversed_dict)