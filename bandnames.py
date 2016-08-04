import random
articles = ["The ","14 ", "23 ", "His ", "Her ", "Two ", "Three ", "Five ", "Seven "]
adjectives = ["Fierce ", "Bloody ", "Screaming ", "Vengeful ", "Raving ", "Jolly ", "Agreeable ", "Pleasant ", "Ecstatic ", "Jubilant "]
nouns = ["Daggers", "Wolves", "Toenails", "Needles", "Clowns", "Bunnies", "Bears", "Kittens", "Clouds", "Hearts"]

articles_length = len(articles)
adjectives_length = len(adjectives)
nouns_length = len(nouns)

random_index1 = random.randint(0, articles_length - 1)
random_index2 = random.randint(0, adjectives_length - 1)
random_index3 = random.randint(0, nouns_length - 1)

counter = 1
while counter <= 10:
		print(counter, ")", articles[random_index1], adjectives[random_index2], nouns[random_index3])
		print("Choose this name? Say 'yes' or 'no'.")
		user_input = input()
		done = False
		while not done:
			if user_input == "yes":
				print("Congrats! Have fun with your band.")
				counter = 11
				done = True
			elif user_input == "no":
				random_index1 = random.randint(0, articles_length - 1)
				random_index2 = random.randint(0, adjectives_length - 1)
				random_index3 = random.randint(0, nouns_length - 1)
				counter += 1
				done = True
			else:
				print("Please type 'yes' or 'no'.")
				done = True
			