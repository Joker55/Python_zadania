file = open('Zycie.txt')
dictionary_list = {'never':'almost never','or':'and','and':'or'}
read_lines = ''
for word in file.read().split(' '):
	if not word in dictionary_list:
		read_lines += word + ' '
	else:
		read_lines += dictionary_list[word] + ' '
filech = open('Zycie-ch.txt', 'w+')
filech.write(read_lines)
file.close()
filech.close()
print ('./done')






