# Language: Python 3
if __name__ == '__main__':
    scoreList = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoreList.append([name, score])

    unique_numbers = sorted(set(item[1] for item in scoreList))

    second_lowest = unique_numbers[1]

    filtered_items = [item for item in scoreList if item[1] == second_lowest]

    sorted_items = sorted(filtered_items, key=lambda x: x[0])

    for item in sorted_items:
        print(item[0])