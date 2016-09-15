turns=0
import random
number = random.randint(1, 100)
for _ in range(5):
    guess=input("guess a number between 1 and 100")
    guess=int(guess)
    if guess == number:
        print("you are correct")
        turns +=1
        print("you have taken {} turns".format(turns))
        break
    elif guess > number:
        print("{} is too high".format(guess))
        turns +=1
        print("you have taken {} turns".format(turns))
    else:
        print("{} is too low".format(guess))
        turns +=1
        print("you have taken {} turns".format(turns))
