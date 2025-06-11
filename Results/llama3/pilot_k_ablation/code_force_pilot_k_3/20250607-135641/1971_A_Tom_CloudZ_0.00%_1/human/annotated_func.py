#State of the program right berfore the function call: stdin contains a positive integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: `_` is `t`, `a` is an integer between 0 and 9, `b` is an integer between 0 and 9, stdin is empty, and the maximum of `a` and `b` and the minimum of `a` and `b` are being printed

#Overall this is what the function does:The function reads a positive integer t from standard input, followed by t lines, each containing two space-separated integers x and y. It then prints the maximum and minimum of each pair of integers, in that order, for each of the t lines. The function does not return any value, and its purpose is to output the sorted pairs of integers.

