
# task 2.3

def task2_3(char_lst):
    n = int(len(char_lst) ** (1/2))
    output_list = [[None for _ in range(n)] for _ in range(n)]
    left, right, top, bottom = 0, n-1, 0, n-1
    index = 0

    # while left <= right and top <= bottom: 
    while index < n**2:

        for i in range(top, bottom+1):
            print(left)
            print(i)
            output_list[i][left] = char_lst[index]
            index += 1
        left += 1

        for i in range(left, right):
            output_list[bottom][i] = char_lst[index]
            index += 1
        bottom -= 1

        for i in range(bottom + 1, top, -1):
            output_list[i][right] = char_lst[index]
            index += 1
        right -= 1

        for i in range(right+1, left-1, -1):
            output_list[top][i] = char_lst[index]
            index += 1
        top += 1
    for row in output_list:
        print(row)

task2_3('#abcdefghijklmn@')