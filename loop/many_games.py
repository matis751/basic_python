new = [ ]
new.append(input("quelle jeu veux tu ajouter ?"))
while new[-1] != "quit":
    new.append(input("quelle jeu veux tu ajouter ?"))
new.pop()
print(new)

