import random 
print("Hello World")
print()

def age_game():
	try:
		age = input("Your age please: ")
		age = int(age)
	except ValueError:
		print ("Please input a interger!")
		print()
		age_game()
		
	randomnumber = random.randint(1,100)
	randomnumber = int(randomnumber)
	print()
	print("My age is {0}".format(randomnumber))
	print("Player age is {0}".format(age))
	print()
	if age > randomnumber:
		print("Looks like you're older than me !")
	elif randomnumber > age:
		print("Young one, do what you love while you're still young!")
	else:
		print("We are the same age, bet we have similar hobbies")				
	print()
	if age-randomnumber >=12 :
		print("Hello, Mr {0}!".format(age))
		print("Bommer...")
		print("How is it like being old? HAHA")
	elif randomnumber-age >= 12:
		print("Hello, Zoomer,")
		print("I am older than you by {0}!".format(randomnumber - age))	
	else:
		print("{0} is not very far from my age which is {1}, So we are about the same age, similar interest perhaps?".format(age,randomnumber))

age_game()
print()
print("Press run to try again!")

