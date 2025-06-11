#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t lines, each containing three digits (0 <= a, b, c <= 9).
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
        
    #State: `q` is an integer between 0 and 1000, `mn` is 100, `a`, `b`, and `c` are integers between 0 and 9 that were read from the last line of stdin, `i` is `q-1`, stdin is empty. If `a` is less than `b` and `b` is less than `c`, 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, 'PEAK' is printed. If `a` is less than `b` and `b` is equal to `c`, 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:The function reads a series of lines from standard input, where the first line contains an integer (t) and each subsequent line contains three digits (a, b, c). It then classifies each set of three digits into one of three categories: 'STAIR' if a < b < c, 'PEAK' if a < b > c or a < b == c, and 'NONE' otherwise. The function prints the classification for each set of three digits.

