hex_lookup_table = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

binary_to_hex_conversions = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

def decimal_to_binary(decimal_num):
    decimal_num = int(decimal_num)
    power = 0
    while decimal_num//2**power != 1:
        power += 1
    binary_num = ""
    for num in range(power, -1, -1):
        if decimal_num - 2**num >= 0:
            binary_num += "1"
            decimal_num -= 2**num
        else:
            binary_num += "0"
    return binary_num

def binary_to_decimal(binary_num):
    power = len(binary_num) - 1
    decimal_num = 0
    for binary in binary_num:
        if binary == "1":
            decimal_num += 2**power
        power -=1
    return decimal_num

def binary_to_hexadecimal(binary_num):
    binary_num = binary_num[::-1]
    hex_num = ""
    for num_of_four in range((len(binary_num)//4) + 1):
        four_hex = (binary_num[num_of_four*4: (num_of_four*4) + 4])[::-1]
        if len(four_hex) < 4:
            four_hex = ("0"*(4-len(four_hex))) + four_hex
        hex_num = binary_to_hex_conversions[four_hex] + hex_num
    return hex_num

def hexadecimal_to_binary(hex_num):
    binary_num = ""
    for hex in hex_num:
        if not hex.isnumeric():
            hex = hex.upper()
        for key, value in binary_to_hex_conversions.items():
            if value == hex:
                binary_num += key
    for binary in binary_num:
        if binary == "1":
            break
        else:
            binary_num = binary_num[1::]
    return binary_num

def decimal_to_hexadecimal(decimal_num):
    decimal_num = int(decimal_num)
    hex_number = ""
    while decimal_num //16 != 0:
        remainder = decimal_num % 16
        if remainder > 9:
            remainder = hex_lookup_table[remainder]
        hex_number = str(remainder) + hex_number
        decimal_num//=16
    if decimal_num > 9:
        decimal_num = hex_lookup_table[decimal_num]
    hex_number = str(decimal_num) + hex_number
    return hex_number

def hexadecimal_to_decimal(hex_num):
    decimal_num = 0
    hex_num = list(hex_num)
    power = len(hex_num)
    for digit in hex_num:
        power -=1
        if not digit.isnumeric():
            for key, value in hex_lookup_table.items():
                if digit.upper() == value:
                    digit = key
                    break
        decimal_num += int(digit) * 16 ** power
    return decimal_num

def perform_function(function_num, number):
    if function_num == 1:
        print(hexadecimal_to_decimal(number))
    elif function_num ==2:
        print(decimal_to_hexadecimal(number))
    elif function_num ==3:
        print(decimal_to_binary(number))
    elif function_num ==4:
        print(binary_to_decimal(number))
    elif function_num ==5:
        print(binary_to_hexadecimal(number))
    elif function_num ==6:
        print(hexadecimal_to_binary(number))
    else:
        print("Function not specified")

def interface():
    print("Which operation do you need: ")
    print("1: hexadecimal to decimal\n2: decimal to hexadecimal\n3: Decimal to Binary\n4: Binary to decimal")
    print("5: Binary to Hexadecimal\n6: Hexadecimal to Binary")
    fun = int(input(">"))
    print("Please enter your number")
    number = input(">")
    perform_function(fun, number)

while True:
    interface()



