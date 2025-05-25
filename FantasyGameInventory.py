print("Name: Anshikaa A Singh")
print("USN: 1AY24AI011")
print("Section: M")
inventory = {}
while True:
    action = input("Would you like to 'add', 'remove', or 'view' items? (type 'exit' to quit): ").lower()
    if action == 'add':
        item = input("Enter the item you want to add: ")
        quantity = int(input("Enter the quantity: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"{quantity} {item}(s) added to your inventory.")
    elif action == 'remove':
        item = input("Enter the item you want to remove: ")
        if item in inventory:
            quantity = int(input("Enter the quantity: "))
            if quantity >= inventory[item]:
                del inventory[item]
                print(f"{item} removed from your inventory.")
            else:
                inventory[item] -= quantity
                print(f"{quantity} {item}(s) removed from your inventory.")
        else:
            print(f"{item} is not in your inventory.")
    elif action == 'view':
        if inventory:
            print("Your inventory:")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Your inventory is empty.")
    elif action == 'exit':
        break
    else:
        print("Invalid action. Please try again.")
