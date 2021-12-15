def loop_function(pets_name):
    for name, kind in pets_name.items():
        print("now %s is a %s" %(name, kind))



pets_name = {"zigy" : "canary",
"tigrou" : "tigre",
"winy" : "ourson",}

loop_function(pets_name)

pets_name["tigrou"] = "un gros tigre"
loop_function(pets_name)
pets_name["flipper"] = "un dauphin"
loop_function(pets_name)
del pets_name["zigy"]
loop_function(pets_name)

