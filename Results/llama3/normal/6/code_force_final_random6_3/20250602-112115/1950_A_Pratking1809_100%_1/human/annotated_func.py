#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `q` is an integer between 1 and 1000, `i` is `q-1`, `a`, `b`, `c` are integers between 0 and 9, `a`, `b`, `c` are assigned the values of the last line of stdin, stdin is empty. If `a` is less than `b` and `b` is less than `c`, 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, 'PEAK' is printed. If `a` is not less than `b` or `b` is not greater than `c`, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of digits as either 'STAIR', 'PEAK', or 'NONE' based on their relative values, and prints out the corresponding classification. The function processes a number of lines specified by the first input, which is an integer between 1 and 1000.

