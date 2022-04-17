import random 
print("Hello World")


def age_game():
	age = input("Your age please: ")
	age = int(age)

	randomnumber = random.randint(1,100)
	randomnumber = int(randomnumber)

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
		print("How is it like being old? HAHA")
		print("Hello, Mr Boomer!")
	elif randomnumber-age >= 20:
		print("I am older than you!")
		print("Hello, Zoomer")
	else:
		print("We are about the same age, similar interest perhaps?")

age_game()
print()
print("press run to try again!")

