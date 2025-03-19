def squarer(a):
    i = 1
    dict = {}
    while i <= a:
        dict[i] = i * i
        i += 1
    print(dict)
        
user_input = int(input(""))
squarer(user_input)