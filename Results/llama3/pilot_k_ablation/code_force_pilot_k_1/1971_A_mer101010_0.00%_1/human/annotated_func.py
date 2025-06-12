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
        
    #State: `n` is an integer between 1 and 100, `t` is 0, `i` is `n`, `a` and `b` are integers between 0 and 9, and stdin is empty. For each pair of integers (x, y) from the original stdin, either "[x] [y]" or "[y] [x]" is printed, depending on whether x is greater than or less than or equal to y.

#Overall this is what the function does:The function reads an integer `n` from standard input, followed by `n` pairs of integers. It then prints each pair of integers in non-decreasing order, either in the original order if the first integer is greater than or equal to the second, or in reverse order if the first integer is less than the second. The function does not return any value, but instead prints the sorted pairs to standard output.

