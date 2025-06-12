#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: stdin is empty, _ is t, for each line of the input, if `n` equals `k`, a string of '1 ' repeated n times, excluding the last space is printed, if `n` is not equal to `k`, then if `k` is 1, a string of numbers from 1 to n is printed, where each number is separated by a space, otherwise, -1 is printed.

#Overall this is what the function does:This function reads a series of input lines from standard input, where each line contains two integers, n and k. For each line, it checks the values of n and k and prints a specific output based on their relationship. If n equals k, it prints a string of '1' repeated n times. If n does not equal k but k is 1, it prints a string of numbers from 1 to n. In all other cases, it prints -1. The function continues this process until all input lines have been processed, leaving the standard input empty.

