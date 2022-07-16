from Lists import countPosition

def fileRead():
    f = open("notes.txt")
    text = f.read()
    f.close()
    return text

if __name__=="__main__":
    txt = fileRead()
    print(txt)
    search_word = input("Enter Search word: ")
    count = countPosition(txt, search_word)
    if count == False:
        print("Not Present")
    else:
        print('The word "{}" occurs {} times in the file.'.format(search_word, len(count)))
