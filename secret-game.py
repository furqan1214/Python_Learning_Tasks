import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 Correct!")
else:
    print("❌ Wrong. The number was", secret)
