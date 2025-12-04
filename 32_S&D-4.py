# Remove a key-value pair from a dictionary.

data = {}
for i in range(5):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    data[key] = value

remove_key = input("Enter the key to remove: ")
if remove_key in data:
    del data[remove_key]
    print(f"Key '{remove_key}' removed.")
else:
    print(f"Key '{remove_key}' not found.")

print("Updated dictionary:", data)