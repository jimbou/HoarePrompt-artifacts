#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    n = int(input())
    t = 0
    for i in range(n):
        a, b = map(int, input().split())
        
        if a < b:
            print(a, b)
        elif a == b:
            print(a, b)
        else:
            print(b, a)
        
    #State: `n` is an integer between 1 and 100 inclusive, `i` is `n`, `t` is 0, `a` and `b` are integers between 0 and 9. For each pair of `a` and `b` that were read from stdin, either `a` and `b` were printed if `a` is less than or equal to `b`, or `b` and `a` were printed if `a` is greater than `b`.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the first integer represents the number of pairs to read. For each pair, it prints the two integers in ascending order, with the smaller integer first. The function does not return any value, but rather produces output through print statements.

