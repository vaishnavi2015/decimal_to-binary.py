def binary_number(decimal_number):
    number = decimal_number
    result=""
    while number>0:
      remainder=number%2
      result = str(remainder) + result
      number = number//2
    return result
decimal_number = int(input("Enter decimal number:"))
print('binary number=>',binary_number(decimal_number))

