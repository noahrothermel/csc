# learning_python.py

# Read the entire file
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
print("=== Reading the entire file ===")
print(contents.strip())

# Read line by line into a list
print("\n=== Reading line by line ===")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())


# learning_c.py

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())

# simpler_reader.py

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object.read().splitlines():
        print(line)

# guest.py

filename = 'guest.txt'

name = input("What is your name? ")

with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Hello, {name}! Your name has been written to {filename}.")

# guest_book.py

filename = 'guest_book.txt'

print("Enter 'quit' to stop entering names.")

while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        break
    else:
        print(f"Welcome, {name}!")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")

# addition.py

print("Give me two numbers, and I’ll add them together.")

try:
    num1 = input("First number: ")
    num2 = input("Second number: ")
    result = int(num1) + int(num2)
except ValueError:
    print("Oops! Please enter only numbers.")
else:
    print(f"The sum of {num1} and {num2} is {result}.")

# addition_calculator.py

print("Enter two numbers to add. Type 'q' at any time to quit.")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Oops! Please enter valid numbers.")
    else:
        print(f"The sum of {num1} and {num2} is {result}.")


# cats_and_dogs.py

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())

# silent_cats_and_dogs.py

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # Fail silently
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())

# common_words.py

def count_word(filename, word):
    """Count how many times a word appears in a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        count = contents.lower().count(word.lower())
        print(f"The word '{word}' appears about {count} times in {filename}.")

# Example usage:
count_word('alice.txt', 'Alice')
count_word('moby_dick.txt', 'whale')

# favorite_number_write.py
import json

number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)

print(f"Thanks! I’ll remember that your favorite number is {number}.")

# favorite_number_read.py
import json

filename = 'favorite_number.json'

with open(filename) as f:
    number = json.load(f)

print(f"I know your favorite number! It’s {number}.")

# favorite_number_remembered.py
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print(f"Thanks! I’ll remember that your favorite number is {number}.")
else:
    print(f"I know your favorite number! It’s {number}.")

# user_dictionary.py
import json

filename = 'user_info.json'

# Collect user information
username = input("What is your name? ")
age = input("How old are you? ")
favorite_color = input("What is your favorite color? ")

# Store in a dictionary
user_info = {
    'username': username,
    'age': age,
    'favorite_color': favorite_color
}

# Save to a file
with open(filename, 'w') as f:
    json.dump(user_info, f)

print("\nUser information saved!\n")

# Read it back
with open(filename) as f:
    stored_info = json.load(f)

print("Here’s what I remember about you:")
for key, value in stored_info.items():
    print(f"  {key.title()}: {value}")

# verify_user.py
import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name, verifying identity."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We’ll remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We’ll remember you next time, {username}!")

greet_user()
