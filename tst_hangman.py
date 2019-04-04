Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hangman(word):
	wrong = 0
	stages = ["",
		  "_________          ",
		  "|                  ",
		  "|        |         ",
		  "|        O         ",
		  "|       /|\        ",
		  "|       / \        ",
		  "|                  "]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print (" ハングマンへようこそ！")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "predict the word"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print(" ".join(board))
		e = wrong + 1
		print ("\n".join(stages[0:e]))
		if "_" not in board:
			print("you win")
			print("_".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong + 1]))
		print(" you lose. The answer is {}.".format(word))

		
>>> 
