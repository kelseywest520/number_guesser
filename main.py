turns=0

for _ in range(5):
    number=input("guess a number between 1 and 100")
    number=int(number)
    if number==40:
        print("40 is correct")
        turns +=1
        print("you have taken {} turns".format(turns))
        break
    elif number > 40:
        print("{} is too high".format(number))
        turns +=1
        print("you have taken {} turns".format(turns))
    else:
        print("{} is too low".format(number))
        turns +=1
        print("you have taken {} turns".format(turns))
