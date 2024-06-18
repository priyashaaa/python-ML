main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

index = main_string.find(substring)
if index != -1:
    print("The substring is present in the main string at index", index)
else:
    print("The substring is not present in the main string.")