#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: stdin is empty, `_` is equal to the initial value of t, if t is 0, no output is printed, if t is greater than 0, t lines are printed, each line contains either a string of n '1's separated by spaces, a string of numbers from 1 to n separated by spaces, or -1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then prints a specific pattern of numbers based on the values of n and k. If n equals k, it prints a string of n '1's separated by spaces. If k equals 1, it prints a string of numbers from 1 to n separated by spaces. For all other cases, it prints -1. The function continues to read and process test cases until the input is exhausted, at which point it terminates, leaving the input stream empty.

