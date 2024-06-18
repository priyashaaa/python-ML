def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C is {fahrenheit}°F."

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return f"{fahrenheit}°F is {celsius}°C."


print(celsius_to_fahrenheit(30))  
print(fahrenheit_to_celsius(86))  


while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(celsius_to_fahrenheit(celsius))
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(fahrenheit_to_celsius(fahrenheit))
    else:
        print("Invalid choice. Please try again.")