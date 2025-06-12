#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(min(a, b), max(a, b))
        
    #State: `t` is an integer between 1 and 100, stdin is empty, `_` is `t-1`, `a` and `b` are the last two integers read from stdin (0 <= `a`, `b` <= 9), and the minimum and maximum of each pair of integers read from stdin have been printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input integer, and prints the minimum and maximum of each pair.

