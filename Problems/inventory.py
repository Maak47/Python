# inventory.py

# stuff = {'rope': 1,
#          'torch': 6,
#          'gold coin': 42,
#          'dagger': 1,
#          'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # Fill THIS PAT IN
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of Items: " + str(item_total))


# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    inventory = {}
    for invitems in addedItems:
        inventory.setdefault(invitems, 0)
        inventory[invitems] += 1
    return inventory
    for k, v in inventory.items():
        if k in inv:
            inv[k] += inventory[k]
        else:
            inventory[k] = 1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
