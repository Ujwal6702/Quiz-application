from os import chdir
print()
umbrella = 0
while umbrella < 1:
    print("                     ***********Welcome to the Trivia************")
    print()
    print()
    print(" 1. Sports")
    print(" 2. Music")
    print(" 3. Entertainment")
    print(" 4. Politics")
    print(" 5. Harry Potter")
    print(" 6. Lucifer")
    print(" 7. Disney")
    print(" 8. Human Rights")
    print(" 9. Mental Health")
    print("10. Video Games")
    print("11. Create a quiz")
    print("12. User created quiz")
    print()
    variables = int(input("Enter the Topic number: "))
    print()
    if variables == 1:
        from sports import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 2:
        from music import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 3:
        from entertainment import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 4:
        from politics import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 5:
        from Harrypotter import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 6:
        from lucifer import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 7:
        from disney import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 8:
        from hr import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 9:
        from mh import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 10:
        from videogames import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 11:
        from uq import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
    elif variables == 12:
        from rf import *
        print()
        print("Press 1 to go to main menu")
        print()
        nugget = int(input("Enter your selected number: "))
        if nugget == 1:
            umbrella = 0
        else:
            umbrella = 1
