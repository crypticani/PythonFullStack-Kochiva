str = ""
line = ""
while(line!="!wq"):
    line = input("Input line: ")
    if(line=="!wq"):
        break
    str+=line
    str+="\n"

f = open("notes.txt", "w")
f.write(str)
f.close()