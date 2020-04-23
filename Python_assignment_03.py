'''Task:
Find out if a given number is an "Armstrong Number".

    An n-digit number that is the sum of the nth powers of
    its digits is called an n-Armstrong number. Examples :

    371 = 33 + 73 + 13;
    9474 = 94 + 44 + 74 + 44;
    93084 = 95 + 35 + 05 + 85 + 45.


    Write a Python program that;

    takes a positive integer number from the user,
    checks the entered number if it is Armstrong,
    consider the negative, float and any entries other than
    numeric values then display a warning message to the user.
'''
while 1:
    total = 0
    num = input("Enter a number: ")
    if num.isdecimal():
        power = len(num)
        for digit in num:
            total += int(digit)**power
            # print(total)
        if int(num) == total:
            print(num, " is an Armstrong number")
        else:
            print(num, " is not an Armstrong number")
    else:
        print("Invalid enter, retry")