#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three digits a, b, c (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `i` is `t-1`, `a`, `b`, `c` are integers between 0 and 9 (inclusive) and are the last line of input from stdin, stdin is empty. If `a` < `b` < `c`, then 'STAIRS' is printed. If `a` < `b` and `b` > `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of inputs from the standard input, where the first input is the number of test cases (t), followed by t lines each containing three digits (a, b, c). It then classifies each set of three digits into one of three categories: 'STAIRS' if a < b < c, 'PEAK' if a < b > c, or 'NONE' otherwise. The classification result is printed to the standard output for each set of three digits. The function does not return any value, and its purpose is to provide a classification output based on the input values.

