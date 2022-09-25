# convert number to romansnumber
# a dictionary with numbers and equals romannumbers declared
roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

# while loop is defined for converting number to romannumber
while True :
    num_to_roman = ''
    try:
        # take a number from user
        decimal_num = int(input("Please Enter a number , Enter 0 to Quit : "))
        if decimal_num == 0:
            break
        if decimal_num > 0 and decimal_num < 4000 :
            for i in roman.keys():
                num_to_roman += roman[i] * (decimal_num//i)
                decimal_num %= i
            result = num_to_roman
        else:
            print("Not Valid Input !!!  Please enter a number from 1 to 4000")
    except ValueError:
        print("Not Valid Input !!!  Please enter a number from 1 to 4000")


# display result
print(f'the result of {decimal_num} is {result}')
