import math


print("Enter the credit principal:")
prin = int(input())

print("What do you want to calculate?")
print("type \"m\" - for count of months,")
print("type \"p\" - for monthly payment:")

choice = input()

if choice == "m":
    print("Enter monthly payment:")
    paym = int(input())
    months = math.ceil(prin / paym)
    if months == 1:
        print("It takes 1 month to repay the credit")
    else:
        print("It takes " + str(months) + "months to repay the credit")
elif choice == "p":
    print("Enter count of months:")
    months = int(input())
    paym = math.ceil(prin / months)
    last_paym = prin - (months - 1) * paym
    if paym == last_paym:
        print("Your monthly payment = " + str(paym))
    else:
        print("Your monthly payment = " + str(paym) + " with last month payment = " + str(last_paym))
