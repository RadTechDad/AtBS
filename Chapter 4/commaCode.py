# commaCode.py
# AtBS - Chapter 4
# Code by Darrell Dudics

def commatize(list):
  listLength = len(list)
  if listLength == 0:
    return 'Please provide a non-empty list.'
    
  retVal = ''
  for i in range(listLength):
    #print(len(list))
    #print(str(i) + ': ' + list[i])
    
    if i == len(list) - 2:
      retVal += list[i] + ', and '
    elif i == len(list) - 1:
      retVal += list[i]
    else:
      retVal += list[i] + ', '

  return retVal
  
list1 = ['red', 'blue', 'green', 'cyan', 'yellow', 'magenta', 'black', 'white']
list2 = ['apples', 'bananas', 'tofu', 'cats']
list3 = ['']

commaText = commatize(list3)  
print(commaText)
