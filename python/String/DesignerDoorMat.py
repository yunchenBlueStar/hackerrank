# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,input().split())

dot_index = 2
center_line = N//2

for i in range(N):
    row_Content = ""
    if(i == center_line ):
        row_Content = "WELCOME"
    else:
        for d in range(dot_index):
            if(d == 0):
                row_Content+=".|"
            elif(d == (dot_index - 1)):
                row_Content+="."
            else:
                row_Content+="..|"
             
    print(f"{'-' * ((M-len(row_Content))//2)}{row_Content}{'-' * ((M-len(row_Content))//2)}")

    if(i < center_line):
        dot_index+=2
    elif(i >= center_line):
        dot_index-=2
    
