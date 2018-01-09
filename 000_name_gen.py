import random

names_female = ["Anna", "Barbara", "Cecylia", "Danuta", "Elżbieta", "Felicja", "Grazyna", "Hanna", "Irena", "Jolanta", "Katarzyna", "Lucyna"]
names_male = ["Adam", "Bogdan", "Czesław", "Dariusz", "Edward", "Feliks", "Gustaw", "Henryk"]
last_name = ["Nowak", "Kowalczyk", "Abramowicz", "Krauze"]

while True:
    answer = input("Do you want to choose male or female name? \n1: male \n2: female\n")
    if answer.isdigit():
        if answer == "1":
            print(random.choice(names_male), random.choice(last_name))
            break
        elif answer == "2":
            print(random.choice(names_female), random.choice(last_name))
            break
        else:
            print("Given value it's not 1 or 2, try again")
    else:
        print ("choose 1 or 2")