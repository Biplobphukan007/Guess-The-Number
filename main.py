import art
import random

print(art.logo)
level = input("Enter the level 'easy', 'medium', 'hard': ")
low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

if level == "easy":
    query = 15
elif level == "medium":
    query = 10
elif level == "hard":
    query = 5
else:
    query = 15

ans = False
target = random.randint(low, high)

while query > 0 and ans == False:
    guess = int(input(f"Guess the number between {low} and {high}: "))
    if guess == target:
        ans = True
        print(f"You guessed correct, The target number was {target}")
        break
    elif guess < target:
        print("guess was low")
    else:
        print("guess was higher")
    query -= 1
    print(f"Chances remaining {query}")

if ans == False:
    print(f"You're out of chances, correct number was {target}")


