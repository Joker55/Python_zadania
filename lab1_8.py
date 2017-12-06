from random import randint

numbers = []
i = 0
while (i < 50):
    numbers.append(randint(1,500))
    i = i + 1

print (numbers)


def sortingF(list):
	equal = []
	less = []
	greater = []

	if len(list) > 1:
		pivot = list[0]
		for x in list:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return sortingF(less)+equal+sortingF(greater)
	else:
		return list

print ('Sorted items: ')
print (sortingF(numbers))


print ('Check: ')
print (sorted(numbers))