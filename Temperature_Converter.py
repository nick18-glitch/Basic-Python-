unit = input("celsius or fahrenheit?(C/F) : ")
temp = float(input("Enter temperature : "))

if unit == 'F':
    temp = temp*9/5+32
    print(f"Fahrenheit is : {temp}°F")
elif unit == "C":
    temp = temp-32*5/9
    print(f"celsius is : {temp}°C")
else:
    print(f"{unit} is invalid !")
  
