dic = { "evrest" : {"elevation" : "8,848",
                    "Range" : "himalaya"},

       "k2" : { "elevation" : "8,611",
               "Range" : "cordieres des andes"},

       "kang" : { "elevation" :"8,592",
                 "Range" : "Chaine de l'alaska"},

       "lhoste" : { "elevation" : "8,516",
                   "Range" : "Vallee du grand rift"},

       "makalu": { "elebvation" : "8,485",
                  "Range" : "Caucase" },}

print("the Mountains name : ")
for i in dic:
    print(i)
print("\nMountains elevation\n")
for i in dic:
    for n, t in dic[i].items():
        if n == "elevation":
            print(t)
print("\nThe range of mountain is\n")
for i in dic:
    for n, t in dic[i].items():
        if n == "Range":
            print(t)
