#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains two integers x and y (0 <= x, y <= 10^9, x != y) — the parameters of the sequences.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif k % 2 != 0:
            print(1)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = k - q
            while f & f - 1 != 0:
                l = bin(f).replace('0b', '')
                p = len(l)
                q = 2 ** (p - 1)
                f = f - q
            print(f)
        
    #State: n is an integer greater than or equal to 0, m is an integer greater than or equal to 0, k is a non-negative integer equal to the absolute difference between n and m, i is equal to the number of test cases, stdin is empty. If the absolute difference between n and m (k) is a power of 2, then k is printed for each test case. Otherwise, if k is odd, the number 1 is printed for each test case. If k is even but not a power of 2, the value of a power of 2 is printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers x and y. It calculates the absolute difference k between x and y and prints a value based on the following conditions: if k is a power of 2, it prints k; if k is odd, it prints 1; if k is even but not a power of 2, it prints the largest power of 2 that is less than or equal to k. The function processes all test cases and leaves the standard input empty.

