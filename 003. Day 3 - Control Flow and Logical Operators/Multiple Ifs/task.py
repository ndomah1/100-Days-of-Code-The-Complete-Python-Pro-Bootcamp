print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    photos = input("Do you want photos? (Y/N): ").upper()
    if age <= 12:
        if photos == "Y":
            print("Your final bill is: $8.")
        else:
            print("Your final bill is: $5.")
    elif age < 18:
        if photos == "Y":
            print("Your final bill is: $10.")
        else:
            print("Your final bill is: $7.")
    else:
        if photos == "Y":
            print("Your final bill is: $15.")
        else:
            print("Your final bill is: $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
