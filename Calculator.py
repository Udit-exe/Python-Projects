class Calculator:

    def add(self, a, b):
        sum = a + b
        print(f"Sum of {a} and {b} = {sum}")

    def sub(self, a, b):
        differ = a - b
        print(f"diff of {a} and {b} = {differ} ")

    def mul(self, a, b):
        multi = a * b
        print(f"Multiplication of {a} and {b} = {multi} ")

    def div(self, a, b):
        if b != 0:
            division = a / b
            print(f"Division of {a} and {b} = {division} ")
        else:
            print("Cannot divide by zero. Please enter a non-zero second number.")

def main():
    calc = Calculator()

    while True:
        print('\nOptions:')
        print('1. Add numbers')
        print('2. Subtract numbers')
        print('3. Multiply numbers')
        print('4. Divide numbers')
        print('5. Quit')

        choice = input('Enter your choice : ')

        if choice == '1':
            num1 = int(input('Enter an integer'))
            num2 = int(input('Enter another integer'))
            calc.add(num1,num2)
        elif choice == '2':
            num1 = int(input('Enter an integer'))
            num2 = int(input('Enter another integer'))
            calc.sub(num1,num2)
        elif choice == '3':
            num1 = int(input('Enter an integer'))
            num2 = int(input('Enter another integer'))
            calc.mul(num1,num2)
        elif choice == '4':
            num1 = int(input('Enter an integer'))
            num2 = int(input('Enter another integer'))
            calc.div(num1,num2)
        elif choice == '5':
            print('Exiting the ToDo list program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

main()
