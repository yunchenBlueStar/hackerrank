if __name__ == '__main__': 
    while True:
        try:
            a = int(input())
            assert 0 <= a <= 10**10
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 1 and 10^10")
        else:
            break
    while True:
        try:
            b = int(input())
            assert 0 <= b <= 10**10
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 1 and 10^10")
        else:
            break
            
    print(f"{a+b}")
    print(f"{a-b}")
    print(f"{a*b}")
