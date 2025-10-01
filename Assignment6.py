# 6-1. Person
person = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

print("6-1. Person:")
print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print("\n") 

# 6-2. Favorite Numbers
favorite_numbers = {
    'Michael': 7,
    'Sarah': 3,
    'John': 42,
    'Emily': 9,
    'David': 13
}

print("6-2. Favorite Numbers:")
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
print("\n")

# 6-3. Glossary
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'A collection of ordered items.',
    'dictionary': 'A collection of key-value pairs.'
}

print("6-3. Glossary:")
for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

    # 6-4. Glossary 2
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'A collection of ordered items.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list of items.',
    'string': 'A series of characters.',
    'boolean': 'A data type with only two values: True or False.',
    'if statement': 'A conditional that executes code based on whether a condition is true.',
    'import': 'Used to bring in external modules or libraries.'
}

print("6-4. Glossary 2:")
for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'danube': 'germany'
}

print("6-5. Rivers:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers mentioned:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries mentioned:")
for country in rivers.values():
    print(f"- {country.title()}")

# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people_to_poll = ['jen', 'edward', 'mike', 'laura', 'sarah']

print("\n6-6. Polling:")
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll about your favorite programming language!")

# 6-7. People
person1 = {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28, 'city': 'New York'}
person2 = {'first_name': 'Bob', 'last_name': 'Smith', 'age': 35, 'city': 'Chicago'}
person3 = {'first_name': 'Clara', 'last_name': 'Lee', 'age': 22, 'city': 'San Francisco'}

people = [person1, person2, person3]

print("6-7. People:")
for person in people:
    print(f"\nFull Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

# 6-8. Pets
pet1 = {'animal': 'dog', 'owner': 'Sarah'}
pet2 = {'animal': 'cat', 'owner': 'Michael'}
pet3 = {'animal': 'parrot', 'owner': 'Emma'}

pets = [pet1, pet2, pet3]

print("\n6-8. Pets:")
for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner']}")

# 6-9. Favorite Places
favorite_places = {
    'John': ['Paris', 'New York', 'Tokyo'],
    'Emily': ['London', 'Berlin'],
    'David': ['Sydney']
}

print("\n6-9. Favorite Places:")
for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")

# 6-10. Favorite Numbers (Multiple Values)
favorite_numbers = {
    'Michael': [7, 14],
    'Sarah': [3, 9, 27],
    'John': [42],
    'Emily': [9, 18],
    'David': [13, 26]
}

print("\n6-10. Favorite Numbers:")
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")

# 6-11. Cities
cities = {
    'new york': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'Known as the Big Apple'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Famous for its cherry blossoms'
    },
    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Home to the Eiffel Tower'
    }
}

print("6-11. Cities Information:\n")
