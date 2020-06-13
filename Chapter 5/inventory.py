# inventory.py
# AtBS - Chapter 5
# Code by Darrell Dudics

stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def displayInventory(inventory):
    print('Inventory:')
    
    item_total = 0
    
    for k, v in inventory.items():
        print(str(v) + "\t" + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
