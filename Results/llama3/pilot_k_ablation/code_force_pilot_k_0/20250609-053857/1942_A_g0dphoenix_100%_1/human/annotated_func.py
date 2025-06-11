#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^3).
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: The output state will be a series of lines, each containing a sequence of integers. If n equals k, the sequence will be a series of 1s repeated n times. If k equals 1, the sequence will be a series of consecutive integers from 1 to n. If neither condition is met, the output will be -1. The number of lines will be equal to the value of t in the initial state.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then generates and prints a sequence of integers based on the values of n and k. If n equals k, the sequence is a series of 1s repeated n times. If k equals 1, the sequence is a series of consecutive integers from 1 to n. If neither condition is met, the function prints -1. The function processes multiple test cases and prints the corresponding sequences or -1 for each case.

