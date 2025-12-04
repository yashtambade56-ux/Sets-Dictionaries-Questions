# Word frequency counter from a paragraph (use dict).

paragraph = input("Enter a paragraph: ")
words = paragraph.split()
frequency = {}
for word in words:
    word = word.lower().strip('.,!?;"\'()')
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")