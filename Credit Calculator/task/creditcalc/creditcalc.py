import math


def get_months():
    print("Enter credit principal:")
    prin = int(input())
    print("Enter monthly payment:")
    paym = int(input())
    print("Enter credit interest:")
    interest = float(input()) / 100

    nom_i = interest / 12
    months = math.ceil(math.log(paym / (paym - nom_i * prin), 1 + nom_i))

    months_left = months % 12
    years = int((months - months_left) / 12)

    years = str(years)
    months_left = str(months_left)
    if months == 0:
        if int(years) == 1:
            print("You need " + years + " year to repay this credit!")
        else:
            print("You need " + years + " years to repay this credit!")
    elif int(years) == 0:
        if int(months_left) == 1:
            print("You need " + months_left + " month to repay this credit!")
        else:
            print("You need " + months_left + " months to repay this credit!")
    else:
        if int(months_left) == 1 and int(years) == 1:
            print("You need " + years + " year and " + months_left + " month to repay this credit!")
        elif int(months_left) == 1:
            print("You need " + years + " years and " + months_left + " month to repay this credit!")
        elif int(years) == 1:
            print("You need " + years + " year and " + months_left + " months to repay this credit!")
        else:
            print("You need " + years + " years and " + months_left + " months to repay this credit!")


def get_paym():
    print("Enter credit principal:")
    prin = int(input())
    print("Enter count of periods:")
    months = int(input())
    print("Enter credit interest:")
    nom_i = float(input()) / (100 * 12)

    print("Your annuity payment = " + str(math.ceil(prin * (nom_i * math.pow(1 + nom_i, months)) / (pow(1 + nom_i, months) - 1))) + "!")


def get_prin():
    print("Enter monthly payment:")
    paym = float(input())
    print("Enter count of periods:")
    months = int(input())
    print("Enter credit interest:")
    nom_i = float(input()) / (100 * 12)

    prin = math.ceil(paym * (math.pow(1 + nom_i, months) - 1) / (nom_i * math.pow(1 + nom_i, months)))

    print("Your credit principal = " + str(prin) + "!")


print("What do you want to calculate?")
print("type \"n\" - for count of months,")
print("type \"a\" - for annuity monthly payment,")
print("type \"p\" - for credit principal:")

choice = input()

if choice == "n":
    get_months()
elif choice == "a":
    get_paym()
else:
    get_prin()
