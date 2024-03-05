def swap_case(s):
    returnStr = ""
    for i in s:
        if i.islower():
            returnStr+= i.upper()
        else:
            returnStr+= i.lower()
    return returnStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)