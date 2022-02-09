# Guess the number game
import random
print("Guess the number between 1 and 10")
print("Enter 'e' for exiting")
while True:
    number = random.randint(1,11)
    failures = 1
    while failures < 4:
        user_ans = int(input("Guess: "))
        if user_ans == number:
            break
        else:
            print(f"Wrong! , You now have {3 - failures} chances left..")
            failures += 1

    if user_ans == number:
        print(f"Congratulations! , {user_ans} is the correct number!")
        break
    else: 
        print(f"The correct answer was {number} , Better luck next time!")
        break
