print("     Guess my number game    ")
secret=12
guess=int(input("guess a number between 1 and 20:"))

if guess == secret:
    print("you got it!!")
else:
    print("Nope! the number was",secret)