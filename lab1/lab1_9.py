file = open('Zycie.txt')
delete_list = ['never','and','why','or']
read_lines = ''
for word in file.read().split(' '):
	if not word in delete_list:
		read_lines += word + ' '
filech = open('Zycie-ch.txt', 'w+')
filech.write(read_lines)
file.close()
filech.close()
print ('./done')
		
