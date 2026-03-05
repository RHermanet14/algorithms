warehouse_inventory = {"Fridge": 5, "Chest Freezer": 8, "Stove": 3, "Dishwasher":1, "Bolt":700}

# basic hashmap functions
def add(name, quantity):
    warehouse_inventory[name] = quantity

def remove(name):
    return warehouse_inventory.pop(name, "Not Found")

def get(name): # should return quantity
    try:
        return warehouse_inventory[name]
    except KeyError:
        print("Item specified does not exist")
        return -1 # might keep at none in case inventory discrepency

def change(name, quantity):
    try:
        old_quantity = warehouse_inventory[name] # intentionally throw error if doesn't exist
        warehouse_inventory[name] = quantity
    except KeyError:
        print("Item specified does not exist")

# functions that implement basic functions
def first():
    print(get("Fridge"))
    print(remove("Fridge"))
    print(get("Fridge"))
    add("Toaster", 50)
    print(get("Toaster"))
    change("Taoseter", 20)
    change("Toaster", 25)
    print(get("Toaster"))

# main logic
first()