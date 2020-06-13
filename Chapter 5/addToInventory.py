# addToInventory.py
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
    print("\nTotal number of items: " + str(item_total))

# displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] += 1
    return inventory
    
inv = {
    'gold coin': 42,
    'rope': 1
}

dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
    ]

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
