# Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, 
# Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
age =int(input("Enter your age : "))
match age:
    case age if age <10:
        print()
        print(" You are a kid! ")
    case age if 10<=age<20:
        print()
        print("You are a teen by age! ")
    case age if 20<=age<40:
        print()
        print("You are a young by age! ")
    case age if 40<=age<60:
        print()
        print("You are a experienced by age! ")
    case age if 60<=age:
        print()
        print("You are a senior citizen! ")
    case _ :
        exit()
print()
     
