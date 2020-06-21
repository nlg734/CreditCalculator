import math
import sys


def get_months(prin, paym, interest):
    #  print("Enter credit principal:")
    prin = int(prin.split("=")[1])
    #  print("Enter monthly payment:")
    paym = int(paym.split("=")[1])
    #  print("Enter credit interest:")
    interest = float(interest.split("=")[1]) / 100

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

    print()
    overpayment = (paym * months) - prin
    print("Overpayment = " + str(overpayment))


def get_paym(prin, months, i):
    #  print("Enter credit principal:")
    prin = int(prin.split("=")[1])
    #  print("Enter count of periods:")
    months = int(months.split("=")[1])
    #  print("Enter credit interest:")
    nom_i = float(i.split("=")[1]) / (100 * 12)

    paym = math.ceil(prin * (nom_i * math.pow(1 + nom_i, months)) / (pow(1 + nom_i, months) - 1))
    print("Your annuity payment = " + str(paym) + "!")
    print()
    overpayment = (paym * months) - prin
    print("Overpayment = " + str(overpayment))


def get_prin(paym, months, i):
    #  print("Enter monthly payment:")
    paym = float(paym.split("=")[1])
    #  print("Enter count of periods:")
    months = int(months.split("=")[1])
    #  print("Enter credit interest:")
    nom_i = float(i.split("=")[1]) / (100 * 12)

    prin = math.ceil(paym * (math.pow(1 + nom_i, months) - 1) / (nom_i * math.pow(1 + nom_i, months)))

    print("Your credit principal = " + str(prin) + "!")
    print()
    overpayment = (paym * months) - prin
    print("Overpayment = " + str(overpayment))


def check_ann_type(params):
    payment = False
    principal = False
    periods = False
    interest = False
    for item in params:
        if item.startswith("--pay"):
            if float(item.split("=")[1]) < 0:
                return "Incorrect parameters"
            payment = True
        elif item.startswith("--prin"):
            if float(item.split("=")[1]) < 0:
                return "Incorrect parameters"
            principal = True
        elif item.startswith("--per"):
            if float(item.split("=")[1]) < 0:
                return "Incorrect parameters"
            periods = True
        elif item.startswith("--int"):
            if float(item.split("=")[1]) < 0:
                return "Incorrect parameters"
            interest = True

    if not interest:
        return "Incorrect parameters"
    if interest and payment and principal:
        return "n"
    if interest and payment and periods:
        return "p"
    if interest and principal and periods:
        return "a"


def check_diff_params(params):
    payment = True
    for item in params:
        if item.startswith("--pay"):
            payment = False
        elif item.startswith("--prin"):
            if float(item.split("=")[1]) < 0:
                return False
        elif item.startswith("--per"):
            if float(item.split("=")[1]) < 0:
                return False
        elif item.startswith("--int"):
            if float(item.split("=")[1]) < 0:
                return False
    return payment


def diff_payment(prin, per, interest):
    prin = int(prin.split("=")[1])
    per = int(per.split("=")[1])
    nom_i = float(interest.split("=")[1]) / (100 * 12)
    total = 0
    for m in range(1, per + 1):
        monthly_paym = math.ceil((prin / per) + nom_i * (prin - (prin * (m - 1)) / per))
        total += monthly_paym
        print("Month " + str(m) + ": paid out " + str(monthly_paym))
    print()
    overpayment = total - prin
    print("Overpaymen = " + str(overpayment))


"""print("What do you want to calculate?")
print("type \"n\" - for count of months,")
print("type \"a\" - for annuity monthly payment,")
print("type \"p\" - for credit principal:")"""

args = sys.argv

if not args[1].startswith("--type") or len(args) != 5:
    print("Incorrect parameters")
elif args[1].split("=")[1] != "diff" and args[1].split("=")[1] != "annuity":
    print("Incorrect parameters")
elif args[1].split("=")[1] == "annuity":
    choice = check_ann_type(args[2:])
    if choice == "n":
        get_months(args[2], args[3], args[4])
    elif choice == "a":
        get_paym(args[2], args[3], args[4])
    elif choice == "p":
        get_prin(args[2], args[3], args[4])
    else:
        print(choice)
elif args[1].split("=")[1] == "diff":
    if check_diff_params(args[2:]):
        diff_payment(args[2], args[3], args[4])
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
