while True:
    print("What do you what to convert? \n1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius")
    scale = input("Choose 1 or 2:")
    temp = int(input("Enter the value"))
    if int(scale) == 1:
        fahr = ((temp * 1.8) + 32)
        print("{} degrees Celsius is {} degrees Fahrenheit".format(temp, fahr))
    elif int(scale) == 2:
        celc = ((temp - 32) / 1.8)
        print("{} degrees Fahrenheit is {} degrees Celsius".format(temp, celc))
    else:
        print("Choose 1. or 2. option")

    one_more = input("\nDo you want to try one more time ? Y/N")
    if one_more == 'Y'or one_more == 'y' or one_more == 'yes' or one_more == 'yep':
        print("\nHere you go again\n")
        continue
    elif one_more == 'N' or one_more == 'n' or one_more == 'no' or one_more == 'hell no':
        print("\ngo away and never come back\n")
        break

