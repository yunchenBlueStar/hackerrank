if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    resultList = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                inner_list = [i, j, k]
                total = sum(inner_list)
                if total != n:
                    resultList.append(inner_list)
                    
    print(resultList)
