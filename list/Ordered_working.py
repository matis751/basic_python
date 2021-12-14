carrers = ["cooker", "prgrammer", "truck driver", "president", "infirmier", "pompier"]
for n in carrers:
	print("print the list in original orer :" + n)
for n in sorted(carrers):
    print("list in alphabetical order " + n)
for n in carrers:
	print("print the list in original order " + n)
for n in sorted(carrers, reverse=True):
	print("print the list in reverse  order " + n)
for i in carrers:
	print("original order of list " + i)
carrers.reverse()
for i in carrers:
    print("list reverse " + i )
carrers.reverse()
for i in carrers:
    print("the list in original order " + i)
carrers.sort()
for i in carrers:
    print("Pently ermansort the list in alphabetical order " + i)

carrers.sort(reverse=True)
for i in carrers:
    print("Pently sort the list in alphabetical reverse order " + i)

