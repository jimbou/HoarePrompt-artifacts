#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `q` is an integer between 1 and 1000 (inclusive), `i` is `q-1`, `a`, `b`, `c` are integers between 0 and 9 (inclusive), `a`, `b`, `c` are assigned the values of the last line of stdin, stdin is empty. If `a` < `b` < `c`, then 'STAIR' is printed. If `a` < `b` and `b` > `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of three digits into one of three categories: 'STAIR' if the digits are in strictly increasing order, 'PEAK' if the first digit is less than the second and the second is greater than the third, and 'NONE' otherwise. The classification is printed to the console for each set of three digits. The function processes a number of lines specified by the first integer read from standard input.

