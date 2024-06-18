message = input("Enter a message: ")
with open("message.txt", "w") as file:
  file.write(message)

print("Message written to message.txt")