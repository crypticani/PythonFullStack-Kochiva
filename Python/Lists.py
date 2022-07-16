def countPosition(str, target):
    result = []
    str = str.split()
    for word in range(0, len(str)):
        if str[word] == target:
            result.append(word)
    if len(result) == 0:
        return False
    else:
        return result


if __name__=="__main__":
    str = input("Enter String: ")
    target = input("Enter target word: ")
    print(countPosition(str, target))
