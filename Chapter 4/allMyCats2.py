# allMyCats2.py
# AtBS - Chapter 4
# Code by Darrell Dudics

catNames = []
while True:
  print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop):')
  name = input()
  if name == '':
    break
  catNames = catNames + [name]  # list concatenation

print('The cat names are:')
for name in catNames:
  print(' ' + name)
