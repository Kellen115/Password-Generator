import random
import string

def create_password(length):

	#defines the allowed characters I can use
	characters = string.ascii_letters + string.digits

	#uses random module to choose characters based on length provided
	password = ''.join(random.choice(characters) for _ in range(length))
	return password

def main():

	#I use a try block to catch any unwanted character outside of regular positive numbers
	try:

		#user input length number as a positive int
		length = int(input("Enter password length: "))

		if length <= 0:
			print("Password must be longer than 0 characters")
			return

		#displays created password for user
		password = create_password(length)
		print(f"\nYour password is: {password}\n")
		print("Congratulations! You have successfully used my app!")

	#except catches any letters or characters where a number should be used instead for the password length
	except ValueError:
		print("Please enter a valid number")

#runs the main function if this code is not being used in another file. Has to be ran directly
if __name__ == "__main__":
	main()