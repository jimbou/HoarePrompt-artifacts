#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: t is an integer between 0 and 47 inclusive, _ is t, n is an integer between 1 and 49 inclusive, stdin contains 0 integers n (1 <= n <= 50). If n is odd, 'NO' is printed. If n is even, 'YES' is printed, a string of 'A's and 'B's of length n is printed, and pattern is a list of 'A's and 'B's of length n, with i being n // 2.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers n. For each n, if n is odd, it prints 'NO'. If n is even, it prints 'YES' followed by a string of alternating 'A's and 'B's of length n. The function processes all t integers and then concludes, leaving the input stream empty.

