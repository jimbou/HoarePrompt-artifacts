#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
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
        
    #State: `n` is an integer equal to `t` (1 <= n <= 100), `t` is 0, `stdin` is empty, `a` and `b` are the last two integers read from `stdin`, `i` is `n-1`. For each pair of integers `x` and `y` (0 <= `x`, `y` <= 9) that were in `stdin`, if `x` is greater than `y`, then "[x] [y]" is printed where [x] is the current value of `x` and [y] is the current value of `y`. If `x` is less than or equal to `y`, then "[y] [x]" is printed where [y] is the current value of `y` and [x] is the current value of `x`. If `x` is equal to `y`, then "[x] [y]" is printed where `x` is equal to `y` and both are between 0 and 9. If `n` is 0, then `stdin` contains `t` lines, each containing two space-separated integers `x` and `y` (0 <= `x`, `y` <= 9) and nothing is printed.

#Overall this is what the function does:This function reads a specified number of pairs of integers from standard input, compares each pair, and prints the pair with the larger number first. If the numbers are equal, it prints them in the order they were read. The function does not return any value but modifies the standard output by printing the sorted pairs.

