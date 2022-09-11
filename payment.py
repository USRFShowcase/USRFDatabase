paygrades = {
    'director': 75.0,
    'executive officer': 70.0,
    'senior field commander': 40.0,
    'field commander': 35.0,
    'senior section leader': 15.0,
    'section leader': 13.0,
    'junior section leader': 9.0,
    'enlisted soldier': 7.0
}


def show_commands():
    for command in command_descriptions:
        command_description = command_descriptions[command]
        print(command_description)


def pay_all():
    for user in users:
        user_paygrade = user['paygrade']
        user['funds'] += paygrades[user_paygrade]
    print('Successfully paid all users.')


def pay_user():
    username_input = get_input('username')
    amount = get_input('amount')
    try:
        amount = float(amount)
    except:
        print('Error. Amount input was not a number.')
        return
    for user in users:
        if user['username'].lower() == username_input:
            user['funds'] += amount
            print(f'Sucessfully paid {username_input} $ND {amount}')
            return
    print(f'Error. Did not find user "{username_input}".')


def print_output(users):
    try:
        with open('users.txt', 'w') as users_txt:
            for index in range(len(users)):
                user = users[index]
                username = user['username']
                user_paygrade = user['paygrade']
                user_funds = user['funds']
                user_string = f'{username}, {user_paygrade}, {user_funds}'
                if index == len(users) - 1:
                    users_txt.write(f'{user_string}')
                    # This is to prevent creating an empty new at the end of the file.
                else:
                    users_txt.write(f'{user_string}\n')
    except:
        print('Could not print database to text file.')


commands = {
    'commands?': show_commands,
    'pay all': pay_all,
    'pay user': pay_user,
}

command_descriptions = {
    'pay all': 'pay all - Pay all users according to their rank.',
    'pay user': 'pay user - Pay a specific user a specific amount.'
}


def get_users(users_txt):
    users = []
    user_lines = users_txt.read().splitlines()
    for line in user_lines:
        user = line.split(', ')
        users.append({
            'username': user[0],
            'paygrade': user[1],
            'funds': float(user[2])
        })
    return users


def get_input(input_type):
    return input(f'Insert {input_type}: ').lower()


def main(users):
    command = get_input('command')
    print()
    if command in commands:
        commands[command]()
    else:
        print(f'[{command}] is not a valid command.')
    print()
    print_output(users)
    main(users)


with open('users.txt', 'r') as users_txt:
    users = get_users(users_txt)
    print('To see a list of commands, type [commands?]')
    main(users)
