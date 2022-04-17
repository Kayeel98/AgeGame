import random 
print("Hello World")


def age_game():
	age = input("Your age please: ")
	age = int(age)

	randomnumber = random.randint(1,100)
	randomnumber = int(randomnumber)

	print("My age is {0}".format(randomnumber))
	print("Your age is {0}".format(age))
	print()
	if age > randomnumber:
		print("Looks like you're older than me !")
	elif randomnumber > age:
		print("Youngling seems like you have more ways to go...")
	else:
		print("We are the samge age, bet we have similar 				hobbies!")
	print()
	if age-randomnumber <= 20:
		print("you could be my father! HAHA")
		print("Hello, Mr Boomer!")
	elif age-randomnumber >= 40:
			print("you could be my grandfather! HAHA")
			print("Hello, Mr Boomer!")
	elif randomnumber-age <= 20:
		print("I could be your father! HAHA")
		print("Hello, Zoomer")
	elif randomnumber-age >= 40:
		print("I could be your grandfather! HAHA")
		print("Hello, Zoomer")
	else:
		print("We are about the same age, similar interest perhaps")



for i in range(3):
	age_game()
	print()