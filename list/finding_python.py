list = "une liste de ;ot contenant au moins deux fois python, comme un python mais pas un python"
print("the sentence is : " + list)
print("Is python word actualy in the sentence ? " + str("python" in list))
index = list.find("python")
print("python appear in the sentence for the first time at index  " + str(index))
index = list.rfind("python")
print("and for the last time at " + str(index))
count = list.count("python")
print("python appear " + str(count) + " times in the sentence")
list.split
print("the raw list : " + list)
for i in list:
	print("the list is split : " + str(i))
list.replace("python", "ruby")
print("lsit")
