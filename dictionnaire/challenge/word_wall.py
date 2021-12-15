def check_file():

    try:
        f = open("words.txt", 'x')
        f.close()
    except (FileExistsError):
        return -1
    return 1

def load_file():
    dic = { }
    file = open("words.txt")
    for line in file:
        index = line.index(' ')
        key = line[: index]
        value = line[index + 1:-1]
        dic[key] = value
    file.close()
    return dic


def All_history(dic):
    print("All the words and definition\n")
    for n, i in dic.items():
        print("'%s' : '%s'" %(n, i))

def definition(dic, word):
    print("Definition:\n'%s' : '%s' " %(word, dic[word]))



def new_f(dic):
    word = input("Write the word you want to add : ")
    for i in dic:
        if i == word:
            print("This word is already in your wall")
            return
    mean = input("Write the definition of the word : ")
    dic[word] = mean
    file = open("words.txt", 'w')
    for n, i in dic.items():
        file.write(n + " " + i + "\n")
    file.close()

def play_f(dic):
    text = ""
    word = input("Which word do you want to try to find the definition ? :")
    for i in dic:
        if i == word:
            while 1:
                if text == "q" or text == "quit":
                    break
                text = input("What is the definition of '%s' ? : " %(i))
                if dic[i] == text:
                    text = input("You win !! Play again ? [Y/N]")
                    if text == "Y" or text == "Yes":
                        play_f(dic)
                    return
                else:
                    text = input("Sorry that is  not the right anser!\nPlay again ? [Y/N] : ")
                    if text != "Y" or "Yes":
                        return()
    print("I don't know this word sorry ...\nTry to add it before and come back !")
    return()


print("\n\n\n\n\n\t\t\t\tWelcome to Word Wall\n\n\n\n")

dic = { }

if check_file() == -1:
    dic = load_file()
print("Enter :\n-'Play' : to play quizz\n-'All history' to see all words and meaning\n-'Definition' to see juste a word\n-'New' to enter a new word and meaning or modify\n-'Quit' or 'q' to leave\n-'Help' or 'h' to see this message again")
while 1 :
    choice = input()
    if choice == "Help" or choice == "h":
        print("Enter :\n-'Play' : to play quizz\n-'All history' to see all words and meaning\n-'Definition' to see juste a word\n-'New' to enter a new word and meaning or modify\n-'Quit' or 'q' to leave\n-'Help' or 'h' to see this message again")
    if choice == "quit" or choice == 'q':
        break
    if choice == "All history":
        All_history(dic)
    if choice == "Definition":
        definition(dic, input("Wich word do you want to learn : "))
    if choice == "New":
        new_f(dic)
    if choice == "Play":
        play_f(dic)
        print("Bye Bye")
