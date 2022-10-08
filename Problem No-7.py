# Write a python program to check whether a given number is positive, negative or zero using match case statement.
num= int(input("Enter the number : "))
match num:
    case num if num>0:
        print("Positive number! ")
    case num if num<0:
        print("Negative number! ")
    case num if num==0:
        print ("Zero number! ")
    case _ :
        exit()
print()
