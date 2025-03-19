sum = 0.0

while True:
    try: 
        
        user_input = int(input())
        
        if user_input == 0:
            print("The grand total is " + str(sum))
            break
        
        sum += user_input
        
        print("The total is now " + str(sum))
    
    except ValueError:
        print("That wasn’t a number.")
        continue