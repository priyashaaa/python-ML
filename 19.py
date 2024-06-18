import string

def remove_punctuations(text):
    result = ""
    for char in text:
        if char not in string.punctuation:
            result += char
    return result

text = "hello! world!! i'm priyasha!!"
print("The original string is :", text)
result = remove_punctuations(text)
print("The string after punctuation filter :", result)