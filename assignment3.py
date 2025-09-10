names = ['Alice', 'Alexander', 'Tyrone', 'John'] 
print(names[0])
print(names[1])
print(names[2])
print(names[3]) 

names = ['Alice', 'Alexander', 'Tyrone', 'John']
print("Hello, " + names[0] + "! Hope you're having a great day!")
print("Hello, " + names[1] + "! Hope you're having a great day!")
print("Hello, " + names[2] + "! Hope you're having a great day!")
print("Hello, " + names[3] + "! Hope you're having a great day!")

cars = ['Tesla Model S', 'Ford Mustang', 'BMW M3', 'Audi A7']
print("I would like to own a " + cars[0] + ".")
print("I would like to own a " + cars[1] + ".")
print("I would like to own a " + cars[2] + ".")
print("I would like to own a " + cars[3] + ".")

guests = ['Patrick Mahomes', 'Tom Brady', 'Odell Beckham Jr.']
print("Dear " + guests[0] + ", you are invited to dinner.")
print("Dear " + guests[1] + ", you are invited to dinner.")
print("Dear " + guests[2] + ", you are invited to dinner.")

guests = ['Patrick Mahomes', 'Tom Brady', 'Odell Beckham Jr.']
print("Dear " + guests[0] + ", you are invited to dinner.")
print("Dear " + guests[1] + ", you are invited to dinner.")
print("Dear " + guests[2] + ", you are invited to dinner.")
print("\nUnfortunately, " + guests[1] + " can't make it to the dinner.")
guests[1] = 'Aaron Rodgers'
print("Dear " + guests[0] + ", you are invited to dinner.")
print("Dear " + guests[1] + ", you are invited to dinner.")
print("Dear " + guests[2] + ", you are invited to dinner.")

guests = ['Patrick Mahomes', 'Aaron Rodgers', 'Odell Beckham Jr.']
print("Good news! We found a bigger dinner table!\n")
guests.insert(0, 'Jalen Hurts')
guests.insert(len(guests)//2, 'Lamar Jackson')
guests.append('Josh Allen')
print("Dear " + guests + ", you are now invited to dinner.")

guests = ['Jalen Hurts', 'Patrick Mahomes', 'Lamar Jackson', 'Aaron Rodgers', 'Odell Beckham Jr.', 'Josh Allen']
print("Unfortunately, the new dinner table wont arrive in time, and I can invite only two people for dinner.\n")
while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry, " + removed_guest + ", I cant invite you to dinner.")
print("\nYou're still invited to dinner:")
for guest in guests:
    print("Dear " + guest + ", you're still invited to dinner.")
    del guests[0]
del guests[0]

guests = ['Jalen Hurts', 'Patrick Mahomes', 'Lamar Jackson', 'Aaron Rodgers', 'Odell Beckham Jr.', 'Josh Allen']
print("I am inviting " + str(len(guests)) + " people to dinner.")

cities = ['Paris', 'Tokyo', 'New York', 'London', 'Sydney']
cities.append('Berlin')
cities.insert(0, 'Amsterdam')
cities.remove('Sydney')
popped_city = cities.pop()
del cities[2]
cities.sort()
cities.reverse()
print("Number of cities in the list:", len(cities))
print("Final list of cities:", cities)
print("The city that was popped:", popped_city)
