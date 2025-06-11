#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: No more input lines are left in stdin, and the loop has finished executing. If `n` equals `k`, a string of '1 ' repeated n times (excluding the last space) has been printed. If `n` is not equal to `k`, then if `k` is 1, a string of numbers from 1 to `n` (inclusive) separated by spaces has been printed. Otherwise, -1 has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it prints a specific output based on the values of n and k. If n equals k, it prints a string of '1 ' repeated n times. If n is not equal to k but k is 1, it prints a string of numbers from 1 to n separated by spaces. For all other cases, it prints -1. The function continues to read and process test cases until all input lines have been consumed.

