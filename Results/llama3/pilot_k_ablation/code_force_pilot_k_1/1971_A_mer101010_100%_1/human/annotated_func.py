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
        
    #State: `n` is an integer between 1 and 100 inclusive, `t` is 0, `i` is `n`, `a` and `b` are the last two integers read from stdin, stdin is empty. For each pair of integers read from stdin, the smaller integer is printed first, followed by the larger integer.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input integer. It then prints each pair with the smaller integer first, followed by the larger integer. The function does not return any value and does not modify any external state except for printing to standard output.

