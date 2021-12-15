dic = { "evrest" : "8,848", "k2" : "8,611", "kang" : "8592", "lhoste" : "8,516", "makalu":"8,485"}
print("The name of mountains")
for i in dic :
	print("Name : %s" %(i))
print("\n")
print("the size of moutains")
for i in dic.values():
	print("Value %s" %(i))
print("\n")
print("Values and size")
for n, i in dic.items():
	print("%s is %s meters tall" %(n, i))
print("\n")

