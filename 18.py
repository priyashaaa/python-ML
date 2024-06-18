def anagrams(str1, str2):
    count1 = {}
    count2 = {}
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    return count1 == count2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if anagrams(str1, str2):
    print("The two strings are anagrams of each other")
else:
    print("The two strings are not anagrams of each other")