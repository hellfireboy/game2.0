import random

print('----------Start Game----------')
randomNumber = random.randint(1, 10)
count = 0
temp = input('You have 5 times to guess a number:')

while not isinstance(temp, int):
    temp = input("You must type a number!")
guess = int(temp)
while guess != randomNumber and count < 5:
    if guess > randomNumber:
        print("That's too big!")
        count = count + 1
        if count != 5:
            print("You still have", 5 - count, "times")
            guess = int(input('Guess a number again:'))
            while not isinstance(guess, int):
                guess = int(input("You must type a number!"))
    else:
        if guess < randomNumber:
            print("That's too small...")
            count = count + 1
            if count != 5:
                print("You still have", 5 - count, "times")
                guess = int(input('Guess a number again:'))
                while not isinstance(guess, int):
                    guess = int(input("You must type a number!"))
if count == 5:
    print("Time's over")
if guess == randomNumber:
    print("You're great! That's right!")
    print("But there's nothing I can give you.")
print("Game is over.")
