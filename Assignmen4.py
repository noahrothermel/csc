pizzas = ['Pepperoni', 'Margarita', 'BBQ Chicken']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

animals = ['Dog', 'Cat', 'Rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")


for number in range(1, 21):
    print(number)


for number in number:
    print(number)

    numbers = list(range(1, 1000001))
    print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")
total_sum = sum(numbers)
print(f"Sum of the numbers: {total_sum}")

for number in range(1, 21, 2):
    print(number)

for number in range(3, 31, 3):
    print(number)

for number in range(1, 11):
    cube = number ** 3
    print(f"The cube of {number} is {cube}")

    cubes = [number ** 3 for number in range(1, 11)]
    print(cubes)


pizzas = ['Pepperoni', 'Margarita', 'BBQ Chicken']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    print("\nThe first three items in the list are:")
print(pizzas[:3])
middle_start = len(pizzas) // 2 - 1
middle_end = middle_start + 3
print("\nThree items from the middle of the list are:")
print(pizzas[middle_start:middle_end])
print("\nThe last three items in the list are:")
print(pizzas[-3:])

my_pizzas = ['Pepperoni', 'Margarita', 'BBQ Chicken']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Hawaiian')
friend_pizzas.append('Vegetarian')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
    print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


izzas = ['Pepperoni', 'Margarita', 'BBQ Chicken']
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    print("\nMy favorite pizzas in uppercase are:")
for pizza in pizzas:
    print(pizza.upper())

    menu = ('Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi')
    print("The restaurant offers the following foods:")
for food in menu:
    print(food)
    menu = ('Pizza', 'Tacos', 'Pasta', 'Steak', 'Ice Cream')
    print("\nThe revised menu is:")
for food in menu:
    print(food)

    print("This is a very long sentence that might go over seventy nine characters if I'm not careful in writing it.")
    print("This is a very long sentence that might go over seventy nine characters ""if I'm not careful in writing it.")
