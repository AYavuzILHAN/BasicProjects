import random

print("Welcome to magical world of the game: Guessing Number Game\n")

number = random.randint(-1000000, 1000000)
deneme = 0
 
while True:
    try:
        guess = int(input("Guess the Number:"))
        if guess > number:
            print("your guess is bigger than number")
            deneme +=1
        elif guess < number:
            print("your guess is smaller than number")
            deneme +=1
        elif guess == number:
             print("You goddamnn right")
             break
    except ValueError:
        print("Please enter the number not words")
        
print("You won the game in {} try".format(deneme))
       