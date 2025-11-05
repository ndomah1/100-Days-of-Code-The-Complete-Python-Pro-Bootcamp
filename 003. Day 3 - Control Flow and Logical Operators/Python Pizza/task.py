print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

if size == "S":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is: $18.")
        else:
            print("Your final bill is: $17.")
    else:
        if extra_cheese == "Y":
            print("Your final bill is: $16.")
        else:
            print("Your final bill is: $15.")
elif size == "M":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is: $24.")
        else:
            print("Your final bill is: $23.")
    else:
        if extra_cheese == "Y":
            print("Your final bill is: $21.")
        else:
            print("Your final bill is: $20.")
elif size == "L":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is: $29.")
        else:
            print("Your final bill is: $28.")
    else:
        if extra_cheese == "Y":
            print("Your final bill is: $26.")
        else:
            print("Your final bill is: $25.")
