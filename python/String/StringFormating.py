def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal_value = str(i)
        octal_value = oct(i)[2:]
        hexadecimal_value = hex(i)[2:].upper()
        binary_value = bin(i)[2:]
        print(decimal_value.rjust(width),octal_value.rjust(width),hexadecimal_value.rjust(width),binary_value.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)