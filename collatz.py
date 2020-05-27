def isEven(number):
  return not int(number) % 2  

def isOdd(number):
  return int(number) % 2

def collatz(number):
  if isEven(number):
    value = number // 2
    print(value)
    return value
  else:
    value = 3 * number + 1
    print(value)
    return value

while True:
  print('Please input a number:')
  try:
    inptValue = int(input())
    break
  except ValueError:
    print('\n** Please only use numbers! **\n')
    continue

num = collatz(inptValue)

while num != 1:
  num = collatz(num)
