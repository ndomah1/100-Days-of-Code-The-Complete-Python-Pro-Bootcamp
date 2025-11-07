import random
import my_module

# Testing custom module
print(my_module.my_favorite_number)

# Generate random int
print(random.randint(1, 100))

# Generate 0 < random float < 1
print(random.random())

# Generate 0 < random float < 10
print(random.random() * 10)
print(random.uniform(1, 10))


# PAUSE 1 - Heads or Tails
coin = random.randint(0, 1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
