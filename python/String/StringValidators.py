if __name__ == '__main__':
    s = input()
    
    isAlnum = False
    isAlpha = False
    isDigit = False
    isLower = False
    isUpper = False
    
    for i in s:
        if(i.isalnum()):
            isAlnum = True
        if(i.isalpha()):
            isAlpha = True
        if(i.isdigit()):
            isDigit = True
        if(i.islower()):
            isLower = True
        if(i.isupper()):
            isUpper = True
            
    print(isAlnum)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)