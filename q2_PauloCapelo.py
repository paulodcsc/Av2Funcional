register_user = lambda username, password: open('users.txt', 'a').write(f'{username} {password}\n')

login_user = lambda username, password: 'SUCCESS' if any(line.strip() == f'{username} {password}' for line in open('users.txt')) else 'FAILURE'

while True:
    print("Choose an option:")
    print("1 - Register user")
    print("2 - Log in")
    print("3 - Exit")
    choice = input("Option: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
        print("User registered successfully!")
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        result = login_user(username, password)
        print(result)
    elif choice == '3':
        break
    else:
        print("Invalid option. Please try again.")
