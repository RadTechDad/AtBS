import random

COINFLIPS = 100
EXPERIMENTS = 1000

numberOfStreaks = 0

for experimentNumber in range(EXPERIMENTS):

  # Code that creates a list of 100 'heads' or 'tails' values.
  coinFlips = []
  for i in range(COINFLIPS):
    side = ''
    if random.randint(0,1):
      side = 'H'
    else:
      side = 'T'
    coinFlips.insert(i, side)

#  for flip in coinFlips:
#    print(flip + ' ', end = '')
#  print('\n')

  # Code that checks if there is a streak of 6 heads or tails in a row.
  streakCounter = 0
  for i in range(len(coinFlips)):
    if i == 0:
      streakCounter += 1
      continue
      
    if coinFlips[i] == coinFlips[i - 1]:
      # Continue Streak
      streakCounter += 1
    else:
      # Streak ends
      #print(coinFlips[i-1] + ' x ' + str(streakCounter), end = '    ')
      if streakCounter >= 6:
        numberOfStreaks += 1
      streakCounter = 1
      
    if i == len(coinFlips) - 1:
      if streakCounter >= 6:
        numberOfStreaks += 1
      #print(coinFlips[i] + ' x ' + str(streakCounter))

#print('Streaks: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
