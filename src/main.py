
n =0
while n != 1:
    weight = int(input("Enter your Numeric valu of Weight: "))
    unit = input("Select unit to convert| Exmp- 'L' for pound or 'K' for Kilogram: ")    
    if unit.upper() == "L":
        convert = weight * .45
        print(f"{weight}lb = {round(convert)}kg ")
    elif unit.upper() == "K":
        convert = weight / .45
        print(f"{weight}kg = {round(convert)}lb ")
    else:
        print("Invalid unit input")


