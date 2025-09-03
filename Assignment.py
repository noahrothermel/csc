name = "alex"
print(name)
message = "Noah"
print(message)
print(f"Hello {name}, it was a nice day outside right?")
name = "Alex"
print(name.lower())
print(name.title())
name = "cristiano roanldo"
print(name.lower())
print(name.upper())
print(name.title())
quote = '"In my mind, not just this year, always, I am always the best. And I am always going to say that."'
print(f'{name} once said, {quote}')
famous_person = "cristiano ronaldo"
quote = '"Talent without working hard is nothing"'
message = f'{famous_person} once said, {quote}'
print(message)
name = "\t\n  Jamal  \n\t"
print("Original name with whitespace:")
print(repr(name))  
print("\nName with leading whitespace removed (lstrip()):")
print(repr(name.lstrip()))
print("\nName with trailing whitespace removed (rstrip()):")
print(repr(name.rstrip()))
print("\nName with all surrounding whitespace removed (strip()):")
print(repr(name.strip()))
filename = 'python_notes.txt'
name_without_extension = filename.removesuffix('.txt')
print(name_without_extension)
print(5 + 3)    
print(16 - 8)    
print(2 * 4)    
print(64 / 8)    
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)
favorite_number = 7  
message = f"My favorite number is {favorite_number}."  
print(message)  
filename = 'python_notes.txt'
name_without_extension = filename.removesuffix('.txt')
print(name_without_extension)
import this