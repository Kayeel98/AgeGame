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
		print("Youngling seems like you have more ways to go...")
	else:
		print("We are the samge age, bet we have similar 				hobbies!")
	print()
	if age-randomnumber >=20 :
		print("Hello, Mr Boomer!")
		print("How is it like being old? HAHA")
	elif randomnumber-age >= 20:
		print("Hello, Zoomer")
		print("I am older than you!")	
	else:
		print("We are about the same age, similar interest perhaps?")

age_game()
print()
print("Press run to try again!")

