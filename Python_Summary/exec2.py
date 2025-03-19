def mathGen(a, b):
    print(f'{a} + {b} is {a + b}')
    print(f'{a} - {b} is {a - b}')
    print(f'{a} * {b} is {a * b}')
    print(f'{a} / {b} is {a / b}')
    print(f'{a} % {b} is {a % b}')
    print(f'{a} ^ {b} is {a ** b}')
    
user_input = int(input(""))
user_input2 = int(input(""))
mathGen(user_input, user_input2)