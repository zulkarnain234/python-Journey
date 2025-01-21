# celcius = int(input("Enter temperature in Celcius:"))
# fahrenheit = (celcius*(9/5))+32
# print(f"the {celcius} converted in fahrenheit is {fahrenheit}" )

# now i  want to add selection for C or F
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celcius(C) or Fahrenheit(F)? (Enter C or F): ")

if unit == "C":
    converted_temp = (temp * 9/5) + 32
    print (f" {temp} °C is equal to {converted_temp} °F")
elif unit == "F":
    converted_temp = (temp-32)*(5/9)
    print (f" {temp} °F is equal to {converted_temp} °C")
else:
    print("Invalid input!!! please select (C or F)")
    

