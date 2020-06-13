# prettyCharacterCount.py
# AtBS - Chapter 5
# Code by Darrell Dudics

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
  count.setdefault(character, 0)
  count[character] = count[character] + 1

pprint.pprint(count)

