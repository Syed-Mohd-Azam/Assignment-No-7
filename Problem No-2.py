# Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division.
print("1- Addition ","2- Subtraction ","3- Multiplication ","4- Division ",sep="\n")
print("Enter your choice: (1-4) ")
choice=int(input())
match choice:
    case 1:
        print("Enter two values to get addition : ")
        a,b=int(input()),int(input())
        print("Addition is : ",(a+b))
    case 2 :
        print("Enter two numbers to get subtraction : ")
        a,b=int(input()),int(input())
        if a>b:
            print("Subtraction is : ",(a-b))
        else:
            print("Subtraction is : ",(b-a))
    case 3:
        print("Enter two values to get multiplication : ")
        a,b=int(input()),int(input())
        print("Multiplication is : ",(a*b))
    case 4:
        print ("Enter two values to get division : ")
        a,b=int(input()),int(input())
        print("Division is : ",float((a/b)))
    case _:
        print("Invalid choice.")
print()