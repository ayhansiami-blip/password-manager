while True:
    choice = input('''
===== Password Manager =====

1. Add Password(1)
2. View Passwords(2)
3. Search Password(3)
4. Exit(4)

Choose an option: ''')

    if choice == '1':
        print('Add Password')

        while True:
            website = input('''
Which website do you want to set a password for?
Available Websites:
1. MoonKing.net (1)
2. chatbot.tv (2)
3. ayhan.com (3)
''')
            if website == '1':
                website_choice = 'MoonKing.net'
                print('Website: MoonKing.net')
                break
            elif website == '2':
                website_choice = 'chatbot.tv'
                print('Website: chatbot.tv')
                break
            elif website == '3':
                # I defined this (website_choice) variable because you said you should not change the user input.
                website_choice = 'ayhan.com'
                print('Website: ayhan.com')
                break
            else:
                print('I didn\'t get that, Please try agian...')
        user_name = input('Enter your Username: ')
        while True:
            password_input1 = input('Enter your Password: ')
            password_input2 = input('Enter your password agian: ')
            if password_input1 == password_input2:
                main_password = password_input1  # just for being clean for later
                account_info = (f'''-------------------------------------

Website: {website_choice}
Username: {user_name}
Password: {main_password}

-------------------------------------
''')
                storage = open('passwords.txt', 'a')
                storage.write(account_info)
                storage.close()
                print(f'''
You have succesfully difined a new Password for \'{website_choice}\' website,
Website: \'{website_choice}\'
Username: \'{user_name}\'
Password: \'{main_password}\'
''')  # This is ONLY and ONLY to show you that the user's username and password are stored!

                break
            else:
                print('Your Passwords dosen\'t match, please try agian...')
    elif choice == '2':
        print('View Passwords')
    elif choice == '3':
        print('Search Password')
    elif choice == '4':
        print('Exit')
        print('Thank you for using my program XD')
        break
    else:
        print('Didn\'t get that, Please try again.')
