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
        
    #State: `q` is an integer between 1 and 1000, `i` is `q`, `a`, `b`, `c` are integers between 0 and 9, stdin is empty. If `a` is less than `b` and `b` is less than `c`, then 'STAIR' is printed. If `a` is less than `b` and `b` is greater than or equal to `c`, then 'PEAK' is printed. If `a` is not less than `b` or `b` is not greater than `c`, then 'NONE' is printed.

#Overall this is what the function does:The function reads a series of integer triples from standard input, classifies each triple into one of three categories ('STAIR', 'PEAK', or 'NONE') based on the relative values of the integers, and prints the corresponding classification for each triple.

