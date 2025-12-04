# Find common values between two dictionaries.

dict1 = {}
dict2 = {}
for i in range(5):
    key1 = input(f"Enter key {i + 1} for first dictionary: ")
    value1 = input(f"Enter value for {key1}: ")
    dict1[key1] = value1

    key2 = input(f"Enter key {i + 1} for second dictionary: ")
    value2 = input(f"Enter value for {key2}: ")
    dict2[key2] = value2

common_values = set(dict1.values()) & set(dict2.values())
print("Common values between the two dictionaries:", common_values)