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
        
    #State: `n` is an integer and is greater than or equal to 0, `i` is `n`, `t` is 0, `a` and `b` are integers between 0 and 9 inclusive, stdin is empty. The values of `a` and `b` are printed, with `a` printed first if `a` is less than `b`, and `b` printed first otherwise.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input. It then prints each pair, with the smaller number first. If the numbers are equal, it prints them in the order they were input. The function does not return any value, but rather produces output directly to the console.

