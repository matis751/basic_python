dic = { "evrest" : "8,848", "k2" : "8,611", "kang" : "8,592", "lhoste" : "8,516", "makalu":"8,485"}
print("The name of mountains")
for i in sorted(dic) :
	print("Name : %s" %(i))
print("\n")
print("the size of moutains")
for i in sorted(dic.values()):
	print("Value %s" %(i))
print("\n")
print("Values and size")
for n, i in sorted(dic.items()):
	print("%s is %s meters tall" %(n, i))
print("\n")

