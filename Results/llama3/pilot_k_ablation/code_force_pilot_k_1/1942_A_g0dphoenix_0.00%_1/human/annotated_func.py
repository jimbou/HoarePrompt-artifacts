#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        else:
            print(-1)
        
    #State: stdin is empty, `_` is equal to the initial value of t, `n` and `k` are the last pair of integers from the input, a string of '1 ' repeated n times (where n is equal to k) is printed for each pair of n and k where n is equal to k, otherwise -1 is printed for each pair of n and k where n is not equal to k.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair consists of a number n and a number k. If n is equal to k, it prints a string of '1 ' repeated n times. If n is not equal to k, it prints -1. The function continues this process until all pairs of integers have been read from standard input, at which point the input is empty.

