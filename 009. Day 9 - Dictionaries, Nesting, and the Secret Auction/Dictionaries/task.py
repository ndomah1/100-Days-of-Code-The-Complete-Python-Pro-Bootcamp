programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieve a key's element
print(programming_dictionary["Bug"])

# Will throw a 'KeyError'
# print(programming_dictionary["Bog"])

# Add a new key-value pair programmatically
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Initialize an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)                             # Only prints keys
    print(programming_dictionary[key])     # prints current key's value
