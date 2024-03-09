def count_substring(string, sub_string):
    count_substring = 0
    for i in range(0, len(string)):
        if((string[i] == sub_string[0]) and (string[i:i+len(sub_string)] == sub_string) ):
            count_substring += 1
        
    return count_substring

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)