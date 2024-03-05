if __name__ == '__main__':
    N = int(input())
    outputlist = []
    
    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            position = int(command[1])
            value = int(command[2])
            outputlist.insert(position, value)
        elif command[0] == "append":
            value = int(command[1])
            outputlist.append(value)
        elif command[0] == "remove":
            value = int(command[1])
            outputlist.remove(value)
        elif command[0] == "sort":
            outputlist.sort()
        elif command[0] == "pop":
            outputlist.pop()
        elif command[0] == "reverse":
            outputlist.reverse()
        elif command[0] == "print":
            print(outputlist)
        else:
            continue