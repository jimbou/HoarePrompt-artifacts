#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    n = int(input())
    t = 0
    for i in range(n):
        a, b = map(int, input().split())
        
        if a > b:
            print(a, ' ', b)
        elif a == b:
            print(a, ' ', b)
        else:
            print(b, ' ', a)
        
    #State: `n` is an integer between 1 and 100 inclusive, `t` is 0, `i` is `n-1`, `a` and `b` are integers between 0 and 9 inclusive, and are the values of the last line of input from stdin, stdin contains no lines. If `a` is greater than `b`, then "[a] [b]" is printed. If `a` equals `b`, then the values of `a` and `b` are printed. Otherwise, "b a" is printed, where `b` and `a` are the last two integers read from stdin.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input. It then prints each pair, either in the original order if the first integer is greater than or equal to the second, or in reverse order if the first integer is less than the second. The function does not return any value, and its purpose is to reorder and print the input pairs according to the specified condition.

