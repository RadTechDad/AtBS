# myPets.py
# AtBS - Chapter 4
# Code by Darrell Dudics

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()

if name not in myPets:
  print('I do not hae a pet named ' + name)
else:
  print(name + ' is my pet.')
