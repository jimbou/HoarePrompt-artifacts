#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `q` is an integer between 1 and 1000, `mn` is 100, `i` is `q`, `a`, `b`, `c` are integers between 0 and 9, `a`, `b`, `c` are assigned the values of the last three digits from the input, stdin is empty. If `a` is less than `b` and `b` is less than `c`, 'STAIR' is printed. If `a` is less than `b` but `b` is not less than `c`, 'PEAK' is printed. If `a` is not less than `b` or `b` is not less than `c`, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of triple-digit numbers from standard input, determines the pattern of each triplet (either 'STAIR', 'PEAK', or 'NONE'), and prints the corresponding pattern for each triplet. The function processes a specified number of triplets, as indicated by the first integer read from standard input.

