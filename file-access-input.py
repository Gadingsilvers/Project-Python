file = open("coding-1.py", "a")
while True:
	newItem = input("Enter device name: ")
	if newItem == "exit":
		print ("All done!")
		break
	file.write(newItem + "\n")
file.close()
