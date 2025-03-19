def vowelFinder(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sum = 0
    for a in a:
        if a in vowels:
            sum += 1
    print(f'Number of vowels: {sum}')
    
user_input = input("")
vowelFinder(user_input.lower())
