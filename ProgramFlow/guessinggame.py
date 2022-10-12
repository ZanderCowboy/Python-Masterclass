# Video Number: 43, 44, 45, 46, 47, 67, 68
import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Please guess number between 1 and {} (0 to quit): ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it the first time")
elif guess == 0:
    print("Quiting")
else:
    while guess != 0:
        if guess == answer:
            print("Well done, you guessed it")
            break
        else:
            if guess < answer:
                print("Please guess higher")
            else:   # guess must be greater than answer
                print("Please guess lower")
            guess = int(input())

    if guess == 0:
        print("Quiting")
