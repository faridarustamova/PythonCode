#Giving all the information about the AREA(Azerbaijan Robotics Engineering Academy)
import datetime
import random

#Entering personal informations
userFullNames=[]
ages=[]
users_emails=[]
users_phones=[]
userIDNumbers=[]
suitable_prgs=[]

while(input("Do you want to enter new customer(Yes/No)").lower()!='no'):
    userName = input("""Welcome to the AREA(Azerbaijan Robotics Engineering Academy).
Please, enter your first name:""").strip()
    userSurname = input("Please, enter your last name:").strip()
    userFullName=userName+' '+userSurname
    userFullNames.append(userFullName)
    if len(userFullName.split()) < 2:
        print("It is not your full name.")
    else: 
        #Entering the age
        birthday = input("Please, enter your birthday(mm/dd/yyyy):")
        current_date = datetime.date.today()
        birthDate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
        userAge = current_date.year - birthDate.year
        ages.append(userAge)
        userId=str((random.randrange(10**7,10**8)))
        userIDNumbers.append(userId)
        #Checking if user wants to apply to course 
        userCheck = input("Dear, " + userFullName +". If you want to apply to our course type 'Yes', otherwise type 'No'")

        #Giving information due to the user decision
        if userCheck.lower() == "yes":

            #Giving information about program depends on the age
            if userAge > 19 :
                infr = input("You are not suitable for our course. Do you want to get information about our programs? ")
                users_emails.append("NoSuit")
                users_phones.append("NoSuit")
                suitable_prgs.append("NoSuit")

                if infr.lower() == "yes":
                    print("""We have 6 programs in total. Here is information about them: 
                    Robomente: 4-7 ages children (Description: In this program, children will learn \
to create different models by using lego)
                    Scratch: 8-12 ages children (Description: In this program, \
children will learn to write simple code for creating animations and games)
                    Foster: 8-19 ages children (Description: In this program, children will learn how to code, \
desing and simulate robots and they can participate on World Robot Olimpiads)
                    I am pilot: 8-12 ages children (Description: In this program, children will \
learn all about drones and how to fly them)""")
                else:
                    print("Thank you!")
            else:
                infm = input("You are suitable for our course. Do you want to get information about our programs? ")

                if infm.lower() == "yes":
                    print("""We have 6 programs in total. Here is information about them: 
                    Robomente: 4-7 ages children (Description: In this program, children will learn \
to create different models by using lego)
                    Scratch: 8-12 ages children (Description: In this program, \
children will learn to write simple code for creating animations and games)
                    Foster: 8-19 ages children (Description: In this program, children will learn how to code, \
desing and simulate robots and they can participate on World Robot Olimpiads)
                    I am pilot: 8-12 ages children (Description: In this program, children will \
learn all about drones and how to fly them)""")

                    if userAge > 4 and userAge <=7:
                        suitable_prg = input("You are suitable for 'Robomonte' program. Do you want to apply?")
                        suitable_prgs.append("Robomonte")
                    elif userAge >= 8 and userAge <= 12:
                        suitable_prg = input("You are suitable for 'I am pilot', 'Genesis', 'Foster' and 'Scratch' program. \
                        Which program do you want to apply for?")
                        suitable_prgs.append("Scratch")
                    elif userAge >= 13 and userAge <= 19:
                        suitable_prg = input("You are suitable for 'Foster' program. Do you want to apply?")
                        suitable_prgs.append("Foster")
                    #Giving information about branches
                    if suitable_prg.lower() == "yes":
                        branches_region = "Which city is suitable for you to join: Baku, Zakatala, Ganja or Shaki"
                        if branches_region.lower() == "baku":
                            print("We have 5 branches in Baku: Narimanov, Binagadi Youth House, Nizami, Bakikhanov")

                            #Entering email addres and phone number
                            user_email = input("Please, enter your email addres:")
                            user_phone = input("Please, enter your phone number:")
                            users_emails.append(user_email)
                            users_phones.append(user_phone)
                            print("We sent further information about our branches to your phone number and email. \
Thank you!")
                        else:
                            user_email = input("Please, enter your email addres:")
                            user_phone = input("Please, enter your phone number:")
                            users_emails.append(user_email)
                            users_phones.append(user_phone)
                            print("We sent further information about our branch to your phone number and email. \
Thank you!")
                    else:
                            print("Thank you!") 
                else:
                    print("Thank you!")
        else:
            print("Thank you!")
else:
    print("Good Job!")
    userInf={}
    userInf['UsersFullName']=userFullNames
    userInf['UsersAge']=ages
    userInf['userIDNumber']=userIDNumbers
    userInf['SuitableProgram']=suitable_prgs
    userInf['UsersEmail']=users_emails
    userInf['UsersPhone']=users_phones
    print(userInf)
    