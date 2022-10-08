#Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement.
print(" Enter two strings to check the dictionary order who comes first :  ")
str1,str2=input(" Enter first string: "),input("Enter second string: ")
match str2:
    case str2 if str2==str1:
        print(" Both strings are equal! ")
    case str2 if str2<str1:
        print(" Second string comes first in dictionary order ! The order is : ",str2,str1,sep=" \n ")
    case str2 if str2>str1:
        print("Second string comes after first string in dictionary order! The order is : ",str1,str2,sep=" \n ")
    case _:
        exit()
print()
