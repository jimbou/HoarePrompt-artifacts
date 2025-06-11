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
        
    #State: `n` is an integer between 1 and 100, `t` is 0, `i` is `n-1`, `a` and `b` are integers between 0 and 9 that have been read from the last line of stdin, stdin is empty. The values of `a` and `b` are printed, with the larger value first. If `a` is equal to `b`, the values of `a` and `b` are printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input. It then prints each pair, with the larger number first. If the numbers in a pair are equal, it prints them in the order they were read. The function does not return any value, but rather produces output directly to the console.

