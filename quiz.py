score = 0

def check_guess(guess, answer):
    
    global score
    
    still_guess = True
    
    attempt = 0
    
    while still_guess and attempt <3:
        if guess.lower() == answer.lower():
            print('Correct!')
            score += 1
            still_guess = False
        else:
            if attempt <2:
                guess = input("Sorry, try again")
            attempt += 1
            
    if attempt == 3:
        
        print("The correct answer is " + answer)

guess1 = input("Which bear lives in the North Pole?")
check_guess(guess1, 'Polar Bear')
guess2 = input("Which animal is faster: cat or cheetah?")
check_guess(guess2, 'cheetah')


print("your score is " + str(score))
