import string


def print_rangoli(size):
    width = (size * 2 - 1) + (size * 2 - 2)
    # your code goes here
    for i in range((size * 2) -1):
        generate_list = set_generate_list(size, i)
        row_content = ""
        for z in range(len(generate_list)):
            if(len(generate_list) > 1):
                if(z == len(generate_list) - 1):
                    row_content += generate_list[z]
                else:
                    row_content += f'{generate_list[z]}-'
            else:
                row_content += generate_list[z]
        print(f"{'-' * ((width-len(row_content))//2)}{row_content}{'-' * ((width-len(row_content))//2)}")  

def set_generate_list(size: int, print_i: int):
    alphabet_list = list(string.ascii_lowercase)
    generate_list = alphabet_list[(size - (print_i + 1)):size]
    generate_list.reverse()
    if(print_i > 0):
        for k in alphabet_list[size - print_i :size]:
            generate_list.append(k)
    if(print_i > (size - 1)):
        
        generate_list = alphabet_list[(print_i - (size - 1) + 1):size]
        generate_list.reverse()

        for k in alphabet_list[(print_i - (size - 1)):size]:
            generate_list.append(k)

    return generate_list
if __name__ == '__main__':
        n = int(input())
        print_rangoli(n)