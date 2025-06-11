#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: `n` is an integer (1 <= n <= 10^3), `k` is an integer (1 <= k <= n), stdin contains no inputs, _ is t-1. If `n` is equal to `k`, a string of n-1 '1 's is printed. If `n` is not equal to `k`, then if `k` is 1, "1 2 3 ... n" is printed. Otherwise, -1 is printed.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where each pair consists of a number n and a number k, and prints a sequence of numbers based on the values of n and k. If n is equal to k, it prints a sequence of n-1 ones. If n is not equal to k but k is 1, it prints a sequence of numbers from 1 to n. Otherwise, it prints -1. The function continues this process until all input pairs have been processed, at which point standard input is empty.

