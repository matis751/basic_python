numbers = [0, 23, 3, 92, 53]
for index, i in (enumerate(numbers)):
	print(" original order " + str(i))
for index, i in enumerate(numbers):
    print("the numbers in increasing order " + str(i))
for index, i in enumerate(numbers):
	print("original order " + str(i))
for index, i  in enumerate(sorted(numbers, reverse=True)):
	print("numbers by decreasing order " + str(i))
for index, i in enumerate(numbers):
	print("original order " + str(i))
numbers.reverse()
for index, i in enumerate(numbers):
    print("the number in the reverse order " + str(i))
numbers.reverse()
for index, i in enumerate(numbers):
	print("original order " + str(i))
for i in sorted(numbers):
    print("permanently sorted number increasing " + str(i))
for i in sorted(numbers, reverse=True):
    print("permanently sorted number in decreasing order " + str(i))
