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
        
    #State: t is still 0, stdin is empty, and the standard output contains n lines, each containing two space-separated integers x and y (0 <= x, y <= 9) where x is less than or equal to y.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, sorts each pair in ascending order, and prints the sorted pairs to standard output. It does not return any value.

