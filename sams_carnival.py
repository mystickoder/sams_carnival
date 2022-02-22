print("Hello Welcome to Sam's Town Carnival")

age = int(input("How old are you? "))
if age >= 12:
    print('You are old enough to ride ')
    
else:
    if age <= 12:
        print("You are not old enough to ride. ")

if age >= 12:
    print("Here is your ticket please proceed to the line.")
    
elif age <= 12:
    print("Rides for your age group are in the orange sections.")
    
print("Thanks for visiting Sam's Town Carnival.")
    