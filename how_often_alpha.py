f = open("./encryption.md",'r')
words_input = f.readline()

alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = alpha.upper()
number = '0123456789'
spc_char = '!#$%&"()*+,-./:;[=]?@\^_`~'
how_often_count = 0
highest	= 0
sec_highest = 0
what_alpha = 0

while (how_often_count != len(alpha)):
	often_value = words_input.count(alpha[how_often_count])
	print alpha[how_often_count] + str(often_value)
	if (often_value	> highest):
		sec_highest = highest
		sec_what_alpha = what_alpha
		highest	= often_value
		what_alpha = how_often_count
	how_often_count	= how_often_count + 1

print "\n\n\n\n\n" + alpha[what_alpha] + " " + str(highest)
print alpha[sec_what_alpha] + " " + str(sec_highest)