print("Welcome to Trader Joe's")

groceries = {}
		
	def add_item():
		item = input("What item would you like to add?")
		quantity = input("How many " + item + "s would you like to add?")
		groceries[item] = quantity

	def update_item():
		update = input("Would you like to update an item? Y or N: ")
		if update == "Y":
			item = input("Which item would you like to update?")
			if item in groceries:
				quantity = input("How many " + item + "s are there now?")
				groceries[item] = quantity
			else:
				print("Item not found")
				new_item = input("Would you like to add " +item + "? Y or N.")
				if new_item == "Y":
					add_item()
		elif update == "N":
			print("Ok")
	def delete_item():
		item = input("Which item would you like to delete?")
		del groceries[item]
	def print_list():
		choice_print = input ("Would you like to print your list? Y or N")
		if choice_print == "Y":
			print(groceries)
			done =  True
		elif choice_print == "N":
			print("Ok. Continue with your list.")
	
done = False
while not done:	
	order = input("Would you like to add an item, update the number of an item, delete an item, or print your list? Type 'add', 'update', 'del', or 'print'.")
	if order == "add":
		add_item()
	elif order == "update":
		update_item()
	elif order == "del":
		delete_item()
	elif order == "print":
		print_list()
			
