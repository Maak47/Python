dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = {}
inv = {'gold coin': 42, 'rope': 1}

for invitems in dragonLoot:
    inventory.setdefault(invitems, 0)
    inventory[invitems] += 1
print(inventory)
# for k, v in inventory.items():
#     inv = inv[k] + inventory[k]
# print(inv)

for k, v in inventory.items():
    if k in inv:
        inv[k] += inventory[k]
    else:
        inv[k] = 1


print(inv)


# dragonLoot = {'spam': 23, 'ham': 2, 'sandwich': 3}
# dragonLoot2 = {'spam': 24, 'sandwich': 4}

# for k in dragonLoot2.keys():
#     if k in dragonLoot:
#         dragonLoot[k] = dragonLoot[k] + dragonLoot2[k]

# print(dragonLoot)
