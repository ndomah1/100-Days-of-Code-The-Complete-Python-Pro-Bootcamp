states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Print first item, 0-based indexing
print(states_of_america[0])

# Print last item
print(states_of_america[-1])

# Add item
states_of_america.append("Puerto Rico")
print(states_of_america[-1])

# Add multiple items
states_of_america.extend(["England", "Paris"])

# Replace an item
states_of_america[1] = "Pencilvania"

# Print first 5 items
print(states_of_america[:5])

# Print last 5 items
print(states_of_america[-5:])
