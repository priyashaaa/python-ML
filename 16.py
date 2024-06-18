def count_character_frequencies(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

s = input("Enter a string: ")
frequencies = count_character_frequencies(s)

print("Character frequencies:")
for char, frequency in frequencies.items():
    print(f"{char}: {frequency}")