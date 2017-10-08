key = int(raw_input("Key ? : "))
if (key > 25):
	key = key % 25
alpha = 'abcdefghijklmnopqrstuvwxy'
words_input = raw_input("Decrypt this : ")
words = words_input.split()
count_words = 0
new_words = ''
while (count_words != len(words)):
	word = words[count_words]
	count_letter = 0
	new_word = ''
	while (count_letter != len(word)):
		letter = word[count_letter]
		letter_where = alpha.find(letter)
		replace_key = letter_where-key
		if (replace_key > 25):
			replace_key = (replace_key) % 25
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