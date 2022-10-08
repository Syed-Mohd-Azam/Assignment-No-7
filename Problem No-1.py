# Write a python script to display the number of days in a given month number.
month=int(input("Enter the month number: "))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("Days in this month: 31 days! ")
    case month if month in (4,6,9,11):
        print("Days in this month : 30 days! ")
    case 2:
        print("Days in this month : 28 days or 29 days!")
    case _ :
        print("Invalid month number!")
print()
