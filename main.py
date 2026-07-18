while True:
    choice = input('''
===== Password Manager =====

1. Add Password(1)
2. View Passwords(2)
3. Search Password(3)
4. Exit(4)

Choose an option: ''')

    if choice == '1':
        print('<<Add Password>>')

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
                account_info = f'{website_input}|{user_name}|{main_password}\n'
                with open("passwords.txt", "a", encoding="utf-8") as storage:
                    storage.write(account_info)
                print(f'''
You have succesfully difined a new Password for \'{website_input}\' website,
Website: \'{website_input}\'
Username: \'{user_name}\'
Password: \'{censored_password}\'
''')

                break
            else:
                print('Your Passwords dosen\'t match, please try agian...')
    elif choice == '2':
        print('<<View Passwords>>')
        try:
            with open("passwords.txt", "r", encoding="utf-8") as storage:
                for line in storage:
                    website, username, password = line.split('|')
                    print('------------------------------------------')
                    print(f'Website: {website}')
                    print(f'Uesrname: {username}')
                    print(f"Password: {'*' * (len(password) - 1)}")
                    print('------------------------------------------')
        except FileNotFoundError:
            print('You haven\'t set a Password yet...')
    elif choice == '3':
        print('<<Search Password>>')
        exit_program = False
        while True:
            search_choice = input('''1.Search by Website
2.Search by Username
Choose an option: ''')
            if search_choice == '1':
                print('<Search by Website>')
                searched_website = input('Website: ')
                try:
                    with open("passwords.txt", "r", encoding="utf-8") as storage:
                        password_found = False
                        for line in storage:
                            website, username, password = line.split('|')
                            if website != searched_website:
                                continue
                            elif website == searched_website:
                                password_found = True
                                print('------------------------------------------')
                                print(f'Website: {website}')
                                print(f'Uesrname: {username}')
                                print(f"Password: {'*' * (len(password) - 1)}")
                                print('------------------------------------------')
                                show_password_choice = input(
                                    'Show Password? ((Y)es, (N)o)')
                                if show_password_choice.lower() == 'y':
                                    print(
                                        '------------------------------------------')
                                    print(f'Website: {website}')
                                    print(f'Uesrname: {username}')
                                    print(f'Password: {password}')
                                    print(
                                        '------------------------------------------')
                                    search_password_continue_choice = input(
                                        'Do you want to continue to Search Password? ((Y)es, (N)o): ')
                                    if search_password_continue_choice.lower() == 'y':
                                        break
                                    elif search_password_continue_choice.lower() == 'n':
                                        exit_program = True
                                        break
                                    else:
                                        print('Didn\'t get that...')
                                elif show_password_choice.lower() == 'n':
                                    search_password_continue_choice = input(
                                        'Do you want to continue to Search Password? ((Y)es, (N)o): ')
                                    if search_password_continue_choice.lower() == 'y':
                                        break
                                    elif search_password_continue_choice.lower() == 'n':
                                        exit_program = True
                                        break
                                    else:
                                        print('Didn\'t get that...')
                        if not password_found:
                            print('Psaword not found! ')
                except FileNotFoundError:
                    print('You haven\'t set a Password yet...')
                if exit_program:
                    break
            elif search_choice == '2':
                print('<Search by Username>')

    elif choice == '4':
        print('Exit')
        print('Exiting Password Manager...')
        break
    else:
        print('Didn\'t get that, Please try again.')
