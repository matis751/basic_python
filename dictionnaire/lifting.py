def loop_function(dict):
	for lift, num in dict.items():
		print("i did %s %s times" %(lift, num))

dict = {"pompes" : "10", "tractions" : "15", "squates" :"20", "burpee" : 30 }

loop_function(dict)
dict["pompes"] = "100"
loop_function(dict)
dict["guainage"] = "2 minutes"
loop_function(dict)
del(dict["pompes"])
loop_function(dict)

