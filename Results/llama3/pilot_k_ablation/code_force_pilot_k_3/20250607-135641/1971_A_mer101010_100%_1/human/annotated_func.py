#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
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
        
    #State: `n` is an integer between 1 and 100, `t` is 0, `i` is `n-1`, `a` and `b` are integers between 0 and 9, and their order is determined by whether `a` is less than, equal to, or greater than `b`. If `a` is less than `b`, then "[a] [b]" is printed. If `a` is equal to `b`, then `a` and `b` are printed. If `a` is greater than `b`, then `b` and `a` are printed. stdin is empty.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first integer read. It then prints each pair, with the smaller integer first, to standard output. If the integers in a pair are equal, they are printed in the order they were read. The function does not return any value, and its purpose is to reorder and print the input pairs.

