import random


print("Welcome to the High-Low Game!")
print("--------------------------------")


user_score = 0
NUM_ROUNDS = 5
round = 0


while round < NUM_ROUNDS:
    
    userNumber = random.randint(1, 100)
    computerNumber = random.randint(1, 100)
    round += 1
    
    print("Round: #", round)
    print("The user's number is: ", userNumber)
    guess = input("Do you think your number is higher or lower than the computer's?: ")
    guess = guess.lower()
    if guess in ("higher", "lower"):
        if userNumber > computerNumber and guess == "higher":
            print(f"You are correct, The computer's number was {computerNumber}")
            user_score += 1
        elif userNumber < computerNumber and guess == "lower":
            print(f"You are correct, The computer's number was {computerNumber}")
            user_score += 1
        else:
            if userNumber == computerNumber and guess in ("higher", "lower"):
                print(f"The computer's number was {computerNumber}")
            elif userNumber > computerNumber and guess == "lower":
                print(
                    f"You are incorrect, The computer's number was {computerNumber}"
                )
            elif userNumber < computerNumber and guess == "higher":
                print(f"You are incorrect, The computer's number was {computerNumber}")
        
        print("Score: #", user_score)
        print('\n')
    else:
        print("Invalid input, please enter 'higher' or 'lower'")
        print('\n')
        
    
if user_score > 3:
    print("Great job! You're really good at this!")
elif user_score == 3:
    print("Not bad! You're holding steady.")
else:
    print("Keep trying! Practice makes perfect.")

