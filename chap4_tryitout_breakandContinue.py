# My solution
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

print('method 1')
weight=0
items = []

for item_name,item_value in manifest:
	print('current weight {}'.format(weight))
	if weight >= 100:
		print('breaking loop now in method 1')		
		break
	else:
		weight += item_value
		items.append(item_name)
		print('the item being appended are {}'.format(item_name))
print('total weight in the list {}'.format(weight))
print('items in the list are {}'.format(items))


print('method 2')
weight=0
items = []

for item_name,item_value in manifest:
	print('the current weight is {}'.format(weight))
	if weight >= 100:
		print('breaking the loop')
		break
	elif weight + item_value >= 100:
		print('continuing the iteration to the next value as total weight increases')
		continue
	else:
		weight += item_value
		items.append(item_name)
		print('the item being appended to the list is {}'.format(item_name))
print('final weight {}'.format(weight))
print('final list is {}'.format(items))



# Provided Solution
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))
