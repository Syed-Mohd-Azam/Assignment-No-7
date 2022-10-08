# Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not.
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not.
# c. Check whether a given set of three numbers are equilateral triangle or not.
# d. Exit.
print("1- To check whether triangle is isosceles triangle : ")
print("2- To check whether triangle is right angled triangle : ")
print("3- To check whether triangle is equilateral triangle : ")
choice = int(input("Enter your choice (1-3) : "))
match choice:
    case 1:
        print(" Enter the values of three sides of triangle : ")
        a,b,c=float(input()),float(input()),float(input())
        if (a==b or a==c) or (b==c or b==a) or (c==a or c==b):
            print("Given triangle is isosceles triangle .")
        else:
            print("Given triangle is not isosceles triangle. ")
    case 2:
        h=float(input("Enter hpotenuse of triangle : "))
        b=float(input("Enter base of triangle: "))
        p=float(input("Enter perpendicular of triangle : "))
        if ((h*h)==(b*b)+(p*p)):
            print("Given triangle is right angled triangle .")
        else:
            print("Given triangle is not right angled triangle .")
    case 3:
        print ("Enter the values of triangles : ")
        a,b,c=float(input()),float(input()),float(input())
        if (a==b and a==c):
            print("Given triangle is equilateral triangle . ")
        else :
            print("Given triangle is not equilateral triangle . ")
    case _:
        exit()
print()
