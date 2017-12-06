import os

for file in os.listdir():
	if file.split('.')[-1] == 'jpg':
		os.rename(file, file.replace('jpg', 'png'))