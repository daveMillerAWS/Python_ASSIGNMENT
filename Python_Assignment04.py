'''

Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

'''

while True:
    result = "is not a prime number"
# INPUT
    num = input("Enter a number: ")
# IS PRIME ?
    if num.isdecimal():
        num = int(num)
        if num != 0 and num != 1:
            if num == 2:
                result = "is a prime number"
            else:
                for divider in range(2,num):
                    if num % divider == 0:
                        break
                    result = "is a prime number"
    else:
        print("Invalid Enterance!!! retry ")
    print(num,result)
