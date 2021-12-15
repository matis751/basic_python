def function_name(name):
    greet = ["felicitation", "Genial ", "merci a "]
    for i in greet:
        print("%s %s" %(i, name))
    return

list_name = input()
name = list_name.split(' ')
for i in name:
    function_name(i)
