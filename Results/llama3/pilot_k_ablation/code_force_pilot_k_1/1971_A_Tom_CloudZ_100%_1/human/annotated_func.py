#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t lines, each containing two space-separated integers (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(min(a, b), max(a, b))
        
    #State: `t` is an integer between 1 and 100 inclusive, stdin is empty, `a` and `b` are the last two integers read from stdin (0 <= a, b <= 9), and the minimum and maximum of all pairs of integers read from stdin have been printed.

#Overall this is what the function does:This function reads a specified number of pairs of integers from standard input, prints the minimum and maximum of each pair, and empties the standard input buffer. It does not return any value.

