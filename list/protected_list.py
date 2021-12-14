name = ["raisin", "pomme", "banane"]
slice = name[:]
slice.append("fraise")
slice.append("kiwi")
for i in name:
	print("the original list name is " + i)
for i in slice:
	print("the new list name is " + i)
