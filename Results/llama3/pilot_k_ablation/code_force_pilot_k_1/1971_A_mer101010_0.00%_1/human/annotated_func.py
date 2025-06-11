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
        
    #State: `n` is an integer between 1 and 100 inclusive, `t` is 0, `i` is `n`, `a` and `b` are integers between 0 and 9 inclusive, and stdin contains 0 lines. For each pair of integers `a` and `b` read from stdin, if `a` is greater than `b`, then "[a] [b]" is printed where [a] is the current value of `a` and [b] is the current value of `b`. If `a` is less than or equal to `b`, then if `a` is equal to `b`, "[a] [b]" is printed where `a` and `b` are equal integers between 0 and 9 inclusive, otherwise "b a" is printed where `b` is an integer between 0 and 9 inclusive and `a` is an integer between 0 and 9 inclusive.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where the number of pairs is specified by an initial integer input. For each pair, it prints the integers in non-decreasing order, with the smaller integer first if they are not equal, and the integers in the same order if they are equal. The function does not return any value and only produces output through printing.

