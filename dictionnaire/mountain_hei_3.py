dic = { "evrest" : {"8,848" : str(8848 * 3.28)},
       "k2" : {"8,611" : str(8611 * 3.28)},
       "kang" : {"8.592" : str(8592 * 3.28)},
       "lhoste" : {"8,516" : str(8516 * 3.28)},
       "makalu": {"8,485" : str(8485 * 3.28) }}
print("The name of mountains")
for i in dic :
	print("Name : %s" %(i))
print("\n")
print("the size of moutains in meters")
for i in dic:
    for n in dic[i]:
        n = n[1 : ]
        print("Value in meters : %s" %(n))
print("\n")
print("the size of moutains in feets")
for i in dic:
    for n in dic[i].values():
        n = n[0] + n[2 : ]
        print("Value in feets : %s" %(n))

print("\nHow tall each mountain is : ")
for i in dic:
    for t, n in dic[i].items():
        print("the %s size is %s in metters and %s feets" %(i, n, t))
print("\n")

