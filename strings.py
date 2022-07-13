def Encrypt(str, key):
    result = []
    for char in str:
        if (char >= 'A' and char <= 'Z'):
            Z = ord("Z")
            if ord(char)+key > Z:
                char = chr(65+key-(Z-ord(char))-1)
            else:
                char = chr(ord(char)+key)
            result.append(char)
        elif(char >= 'a' and char <= 'z'):
            z = ord("z")
            if ord(char)+key > z:
                char = chr(97+key-(z-ord(char))-1)
            else:
                char = chr(ord(char)+key)
            result.append(char)
        else:
            result.append(char)
    return result

if __name__=="__main__":
    text = input("Enter Plain Text: ")
    key = int(input("Enter Shift Value: "))
    cipher = Encrypt(text, key)
    print(*cipher, sep='')
