#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: `_rep` is equal to `t`, stdin is empty, `n` and `k` are integers between 1 and 10^9 (inclusive). If `n` is higher than `k`, 'Bob' is being printed. If `n` is less than `k`, 'Alice' is being printed. If `n` is equal to `k`, 'Bob' is being printed, and either 'Alice' or 'Bob' is printed, and 'Bob' is printed.

#Overall this is what the function does:The function reads a series of input lines from stdin, where the first line contains an integer t, and each of the following t lines contains two integers a and b. It then compares each pair of integers and prints 'Alice' if a is less than b, 'Bob' if a is greater than or equal to b. The function continues this process until all input lines have been processed, at which point stdin is empty.

