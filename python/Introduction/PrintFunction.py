if __name__ == '__main__':
    n = int(input())
    while True:
        try:
            assert 1 <= n <= 150
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 1 and 150")
        else:
            break
    printString = ""
    for i in range(1, n + 1):
        printString += str(i)
    print(printString)
