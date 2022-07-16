def InvertedIndex(str):
    result = {}
    str = str.split(" ")
    i=0
    for word in str:
        if word in result:
            result[word].append(i)
        else:
           result[word] = [i]
        i+=1
    return result

if __name__=="__main__":
    str = input("Enter String: ")
    print(InvertedIndex(str))
