f = open("./encryption.md",'r')
words_input = f.readline()
print "Your Input: " + words_input + "\n"

# declare variables
alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = alpha.upper()
number = '0123456789'
spc_char = '!#$%&"()*+,-./:;[=]?@\^_`~'
how_often_count = 0
highest	= 0
sec_highest = 0
what_alpha = 0

#print words_input.count(alpha[how_often_count])
while (how_often_count != len(alpha)):
	often_value = words_input.count(alpha[how_often_count])
	if (often_value	> highest):
		sec_highest = highest
		sec_what_alpha = what_alpha
		highest	= often_value
		what_alpha = how_often_count
	how_often_count	= how_often_count + 1
#print alpha[what_alpha] + " " + str(highest)
#print alpha[sec_what_alpha] + " " + str(sec_highest)
key = what_alpha - 4
if (key > 25):
	key = key % 26
#print key
words = words_input.split()
count_words = 0
none_word = 25
new_words = ''
while (count_words != len(words)):
	word = words[count_words]
	count_letter = 0
	new_word = ''
	status = None
	while (count_letter != len(word)):
		status = None
		letter = word[count_letter]
		letter_where = alpha.find(letter)
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
		replace_key = letter_where-key
		if (replace_key > 25):
			replace_key = (replace_key) % 26
		if (status == "num"):
			if (replace_key > 9):
				replace_key = (replace_key) % 10
			elif (replace_key < 0):
				while(replace_key < 0):
					replace_key = replace_key + 10
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
f = open('./decryption.md','w')
f.write(new_words)
f.close()
print "Decrypted : " + new_words