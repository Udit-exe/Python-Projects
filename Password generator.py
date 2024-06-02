import random
import string

def generatePass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def getPassLength():
    while True:
        try:
            return int(input("Enter the password length: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Password Generator!")

    while True:
        length = getPassLength()
        password = generatePass(length)

        print(f"Generated password: {password}")

        another_one = input("Generate another password? (yes/no): ").lower()
        if another_one not in ('yes','y'):
            print("Thank you for using the Password Generator.")
            break

main()
