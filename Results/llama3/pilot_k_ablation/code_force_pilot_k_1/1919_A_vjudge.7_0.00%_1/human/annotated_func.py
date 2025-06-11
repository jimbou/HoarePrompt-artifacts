#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: `t` is 0, stdin is empty, `_rep` is `t` (the initial value of `t`), and the output will contain `t` lines, each containing either 'Alice' or 'Bob', depending on the comparison of `n` and `k` for each input line.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains two integers a and b. It compares each pair of integers and prints 'Alice' if a is less than b, 'Bob' if a is greater than b, or 'Bob' if a is equal to b. The function continues this process until all input lines have been processed, resulting in t lines of output, each containing either 'Alice' or 'Bob'.

