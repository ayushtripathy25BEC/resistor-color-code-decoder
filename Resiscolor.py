# Resistor Color Code Decoder
color_code = { "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
multiplier = {"black": 1, "brown": 10, "red": 100,"orange": 1000, "yellow": 10000,"green": 100000, "blue": 1000000}
print("Resistor Color Code Decoder")
band1 = input("Enter first color: ").lower()
band2 = input("Enter second color: ").lower()
band3 = input("Enter multiplier color: ").lower()
if band1 in color_code and band2 in color_code and band3 in multiplier:
    value = (color_code[band1] * 10 + color_code[band2]) * multiplier[band3]
    print("Resistance =", value, "ohms")
else:
    print("Invalid color entered")