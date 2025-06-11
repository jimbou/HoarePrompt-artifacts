#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 1000) and then a sequence of lines each containing three space-separated integers (between 0 and 9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `n` is an integer between 1 and 1000, `i` is `n-1`, `a`, `b`, and `c` are integers between 0 and 9, stdin contains no input. If `a` is less than `b` and `b` is less than `c`, then 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a sequence of lines from standard input, where the first line contains an integer `n` between 1 and 1000, and each subsequent line contains three space-separated integers `a`, `b`, and `c` between 0 and 9. It then classifies each triplet into one of three categories: 'STAIR' if `a` < `b` < `c`, 'PEAK' if `a` < `b` > `c`, or 'NONE' otherwise, printing the corresponding classification for each triplet. The function does not return any value, and its purpose is to perform this classification and printing task.

