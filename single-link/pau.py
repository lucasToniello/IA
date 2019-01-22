string = input()

while string != "penis":

	if string:
		valores = string.split(" ")

		if string[0] == "c" or string[0] == "k":
			print(valores[0])
		else:
			print("{}\t{}" .format(valores[0] + "0000", valores[1] + "0000"))

	string = input()