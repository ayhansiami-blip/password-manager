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
            website_input = input('Enter your Website address: ')
            website_input = website_input.lower()
            if website_input.strip() == '':
                print('Your Website panel cannot be empty...')
            elif website_input.isdigit():
                print('Your website cannot contain only digits...')
            else:
                print(f'Website: {website_input}')
                break
        while True:
            user_name = input('Enter your Username: ')
            if len(user_name) < 3:
                print('Your username cannot be less then 3 charaters...')
            elif len(user_name) > 30:
                print('Your username cannot be more then 30 charaters...')
            else:
                print(f'Username: {user_name}')
                break
        while True:
            password_input1 = input('Enter your Password: ')
            password_input2 = input('Enter your Password agian: ')
            if password_input1 == password_input2:
                main_password = password_input1  # just for being clean for later
                censored_password = len(main_password) * '*'
                account_info = (f'''-------------------------------------

Website: {website_input}
Username: {user_name}
Password: {main_password}

-------------------------------------
''')
                storage = open('passwords.txt', 'a')
                storage.write(account_info)
                storage.close()
                print(f'''
You have succesfully difined a new Password for \'{website_input}\' website,
Website: \'{website_input}\'
Username: \'{user_name}\'
Password: \'{censored_password}\'
''')  # This is ONLY and ONLY to show you that the user's username and password are stored!

                break
            else:
                print('Your Passwords dosen\'t match, please try agian...')
    elif choice == '2':
        print('View Passwords')
        try:
            with open("passwords.txt", "r") as storage:
                file_content = storage.read()
                print(file_content)
        except FileNotFoundError:
            print('You haven\'t set a Password yet...')
    elif choice == '3':
        print('Search Password')
    elif choice == '4':
        print('Exit')
        print('Exiting Password Manager...')
        break
    else:
        print('Didn\'t get that, Please try again.')
