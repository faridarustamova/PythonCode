#Python program to compute compound interest

import datetime

#Entering personal data
userName = input("            Welcome to the International Bank of Azerbaijan. \nWhat is your name?")
userSurname = input("Hello " + userName.strip() + ".What is your surname?")
date_of_birth = input("Welcome " + userName.strip() + " " + userSurname.strip() + ".Please, enter your birthday(mm/dd/yyyy):")

#Evaluating user age
current_date = datetime.date.today()
birthday = datetime.datetime.strptime(date_of_birth, "%m/%d/%Y").date()
user_age = current_date.year - birthday.year

if user_age >= 18:
    print("You are {0:d}. You can invest your money on our bank".format(user_age))
    
    #Entering numbers to evaluate final amount
    amount_of_money = input("Please, enter the amount of money you want to invest to your account:")
    monthly_int_rate = input("Please, enter the montly interest rate:")
    invest_date = input("When do you want to invest your money?Please, enter date(mm/dd/yyyy):")
    invest_year = datetime.datetime.strptime(invest_date, "%m/%d/%Y").date()
    taking_date = input("When do you want to take your money?Please, enter date(mm/dd/yyyy):")
    taking_year = datetime.datetime.strptime(taking_date, "%m/%d/%Y").date()
    year = taking_year.year - invest_year.year


    #Evaluating the final amount
    final_amount = int(amount_of_money)*(1 + int(monthly_int_rate)/1200)**(int(year)*12)

    print("Your money will be {0:.2f} after {1:d} years".format(final_amount, int(year)))
else:
    print("You are {0:d}.Unfortunately, you can not invest your money on our bank".format(user_age))


