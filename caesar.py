key = int(raw_input("Key ? : "))
if (key > 25):
	key = key % 26
print key
alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = alpha.upper()
number = '0123456789'
spc_char = '!#$%&"()*+,-./:;[=]?@\^_`~'
words_input = raw_input("Encrypt this : ")
words = words_input.split()
count_words = 0
new_words = ''
while (count_words != len(words)):
	word = words[count_words]
	count_letter = 0
	new_word = ''
	while (count_letter != len(word)):
		status = None
		letter = word[count_letter]
		if (letter_where == -1):
			letter_where = upper_alpha.find(letter)
			if (letter_where == -1):
				letter_where = number.find(letter)
				if (letter_where == -1):
					letter_where = spc_char.find(letter)
					status = "spc"
				else:
					status = "num"
			else:
				status = "cap"
		replace_key = letter_where + key
		if (replace_key > 25):
				replace_key = (replace_key) % 26
		if (status == "num"):
			if (replace_key > 9):
				replace_key = (replace_key) % 10
			new_letter = number[replace_key]
		elif (status == "cap"):
			new_letter = upper_alpha[replace_key]
		elif (status == "spc"):
			new_letter = spc_char[replace_key]
		else:
			new_letter = alpha[replace_key]
		new_word = new_word + new_letter
		count_letter = count_letter + 1
		letter_where = 0
	new_word = new_word + " "
	new_words = new_words + new_word
	count_words = count_words + 1
f = open('./encryption.md','w')
f.write(new_words)
f.close()
print "Encrypted : " + new_words