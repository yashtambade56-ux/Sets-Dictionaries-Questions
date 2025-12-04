# Convert two lists (keys, values) into a dictionary.

keys = []
values = []
for i in range(5):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    keys.append(key)
    values.append(value)

dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)