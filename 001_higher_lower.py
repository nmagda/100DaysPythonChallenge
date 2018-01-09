import random

number = random.randint(0,100)
tries = 1
max_tries = 10
while tries <=  max_tries:
    answer = input("Try to guess random number between 0 and 100:")
    if answer.isdigit():
        if int(answer) == number:
            print("Congrats! Random number is ", number, " you have guessed in ", tries, " tries")
            break
        elif int(answer) < number:
            print("Random number is higher, try again")
            tries = tries + 1
        elif int(answer) > number:
            print("Random number is lower, try again")
            tries = tries + 1
    elif answer.isalpha():
        print("You need to enter a number")
        tries = tries + 1
    else:
        print("You need to enter a number")
        tries = tries + 1
    if tries == max_tries:
        print("Looser!")
        break