# Lee Haynes
# Phone: + 44 (0) 785 374 0636
# Email: LeeHaynes2019@yandex.com
# Website: http://www.devcoder.me.uk/
# Instagram: junior_web_developer_2020
# Devcoder Youtube: https://www.youtube.com/channel/UCXqnASrfdoRlyt82YR7n7pQ?view_as=subscriber
# Lee Haynes Youtube: https://www.youtube.com/channel/UCjqLeiVDygmpCHXyeDzH04g
# Git: https://github.com/devcoder2020/python_password_generator


# # Create random password generator, this has been built on the understanding that if the passsword chosen is less than 8 characters, then, the password generetaor is set to a miniimum of 8 charaterts
# So the program is desgined to help with setting the baseline from the strat
import random


# Giving the user the option to check the password file, or, createing a new passweord
print("Do you want to create a password, or, do you want to check you password file?")
assess = input("Make your choice here (check | create)")

if assess == ("create"):
    # This is the minimum length of the password, if you want to set it to less then simply chnage the number here from 8 to whatwever you want 1 or 50, it is your password.
    min_passwd_length = 8

    # Place holder variable
    file = "_"

    # Create the initial text file
    file = open("savedpassword.txt", "a")
    file.close()

    # Created a password list
    password_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!'_+=\"|\"{}:@;'<>,.?/'"

    # Asking user to input a number
    number_characters = int(
        input("Enter the total number of characters for you password "))
    password_output = ""

    # Here is the loop to serch and pick X number of charaters from the password list
    for letters in range(number_characters):
        password_output += random.choice(password_list)
    print(password_output)

    # Here is a password length check
    # If the password is less than 8 then the user will get a prompt asking if they are happy with there password choice if so great if not then a new password will be created
    if (number_characters < min_passwd_length):

        print(
            "#############################################################################")

        print(
            "This is not a good password length, I advise you to increase password length ")

        confirm = input("Are you sure that your happy with the password? ")
        if confirm == "yes".lower() or confirm == "y".lower():
            for letters in range(number_characters):
                password_output += random.choice(password_list)
            print("\/\/\/" * 10)
            print("test after for loop" + password_output)
            print("\/\/\/" * 10)
            print("Do you want to save this password to a file ")
            print()
            print(
                "#############################################################################")
            print()
            print("Do you want to include a username with this password? ")
            print()
            username = input("Enter your Username or Email address here:  ")

            save = input("To save type Y or Yes (y | yes): ").lower()

            if username == "yes".lower() or username == "y".lower():
                file = open("savedpassword.txt", "a")
                file.write("Username or Email: " + username + "\t" +
                           "Random Password: " + password_output + "\n")
                file.close()

            if save == "y".lower() or save == "yes".lower():
                file = open("savedpassword.txt", "a")
                file.write("Username or Email: " + username + "\t" +
                           "Random Password: " + password_output + "\n")
                file.close()
            else:
                print("Your password is:", password_output)

        elif confirm == "no" or confirm == "n":

            print("A stronger password has been chosen for you at random ")
            for letters in range(number_characters+5):
                password_output += random.choice(password_list)
            print(
                "#############################################################################")
            print()
            print("Do you want to save this password to a file? ")
            print()
            print(
                "Do you want to include a username with this password? if not type no or na (no | na) ")
            print()
            username = input("Enter your Username or Email address here:  ")

            save = input("To save type Y or Yes (y | yes): ").lower()

            if username == "yes".lower() or username == "y".lower():
                file = open("savedpassword.txt", "a")
                file.write("Username or Email: " + username + "\t" +
                           "Random Password: " + password_output + "\n")
                file.close()

            if save == "y".lower() or save == "yes".lower():
                file = open("savedpassword.txt", "a")
                file.write("Username or Email: " + username + "\t" +
                           "Random Password: " + password_output + "\n")
                file.close()

            elif username == "na".lower() or username == "no".lower():
                file = open("savedpassword.txt", "a")
                file.write("Random Password: " + password_output + "\n")
                file.close()
            else:
                print("Your password is:", password_output)

        # Here the password is printed to the screen.
        print("Thank you, your password is: ", password_output)

elif assess == ("check"):
    import view_passwords

input("Press any key to continue . . .")
