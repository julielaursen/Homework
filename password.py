import login

def main():
    password = input("Enter your password: ")
    while not login.valid_password(password):
        print("That password is invalid")
        password = input("Enter your password")
    print("That is a valid password")

main()
