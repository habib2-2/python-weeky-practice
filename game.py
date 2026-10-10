
lucky_num = 50

print("Guess the lucky number from 1-70")

user_num = int(input("Enter the lucky number you guessed: "))

while user_num != lucky_num:
    print("Try again")

    if user_num <= 30:
        print("Too low")

    elif user_num < 50:
        print("A little bit close")

    elif user_num > 50:
        print("Too high")

    user_num = int(input("Enter the lucky number: "))

print("=== WINNER ===")