from UI import menu, new_pass, pass_gen
import getpass
import hashlib
import string
import random

account = input("Hi! You're accesing your Password Manager, to proceed choose your account: \n 1 \n 2 \n 3 \n Account: ")
wrongpass = 0
n = 2

if account == "1":
    while wrongpass < 3:
        pass1 = getpass.getpass(prompt='Enter your password: ')
        hashed_password = hashlib.sha256(pass1.encode()).hexdigest()
        if pass1 == 'Pass1':
                print('You\'re in!')
                choice = menu()
                while choice != 'Q':
                    if choice == '1':
                        new_pass()
                    elif choice == '2':
                        find_accounts()
                    elif choice == '3':
                        find()
                    elif choice == '4':
                        print('Here is your new, 8-letter password: \n')
                        password = pass_gen()
                        print(password)
                    elif choice == "Q":
                        exit()
                    else:
                        print('Invalid input')
                        choice = menu()
                    further_choice = input('\n Do you want to return to the menu? Y/N: \n').upper()
                    if further_choice == 'Y':
                        choice = menu()
                    else:
                        exit()
                exit()
        else: 
                if n != 0 :
                    print('Wrong Password, you\'ve got', n, 'remaining tries')
                    wrongpass = wrongpass + 1
                    n = n - 1
                else :
                    print('You\'ve entered an incorrect password 3 times, your access is disabled')
                    exit()

elif account == "2":
    while wrongpass < 3:
        pass2 = getpass.getpass(prompt='Enter your password: ')
        hashed_password = hashlib.sha256(pass2.encode()).hexdigest()
        if pass2 == 'Pass2':
             print('You\'re in!')
             choice = menu()
             while choice != 'Q':
                if choice == '1':
                    new_pass()
                elif choice == '2':
                    find_accounts()
                elif choice == '3':
                    find()
                elif choice == '4':
                    print('Here is your new, 8-letter password: \n')
                    password = pass_gen()
                    print(password)
                elif choice == "Q":
                    exit()
                else:
                    print('Invalid input')
                    choice = menu()
                further_choice = input('\n Do you want to return to the menu? Y/N: \n').upper()
                if further_choice == 'Y':
                    choice = menu()
                else:
                    exit()
             exit()
        else: 
            if n != 0 :
                print('Wrong Password, you\'ve got', n, 'remaining tries')
                wrongpass = wrongpass + 1
                n = n - 1
            else :
                print('You\'ve entered an incorrect password 3 times, your access is disabled')
                exit()

elif account == "3":
    while wrongpass < 3:
        pass3 = getpass.getpass(prompt='Enter your password: ')
        hashed_password = hashlib.sha256(pass3.encode()).hexdigest()
        if pass3 == 'Pass3':
            print('You\'re in!')
            choice = menu()
            while choice != 'Q':
                if choice == '1':
                    new_pass()
                elif choice == '2':
                    find_accounts()
                elif choice == '3':
                    find()
                elif choice == '4':
                    print('Here is your new, 8-letter password: \n')
                    password = pass_gen()
                    print(password)
                elif choice == "Q":
                    exit()
                else:
                    print('Invalid input')
                    choice = menu()
                further_choice = input('\n Do you want to return to the menu? Y/N: \n').upper()
                if further_choice == 'Y':
                    choice = menu()
                else:
                    exit()
            exit()

        else: 
            if n != 0 :
                print('Wrong Password, you\'ve got', n, 'remaining tries')
                wrongpass = wrongpass + 1
                n = n - 1
            else :
                print('You\'ve entered an incorrect password 3 times, your access is disabled')
                exit()

else:
    quit

#changes changes changes


# choice = menu()
# while choice != 'Q':
#     if choice == '1':
#         new_pass()
#     if choice == '2':
#         find_accounts()
#     if choice == '3':
#         find()
#     else:
#         print('Invalid input')
#         choice = menu()
# exit()