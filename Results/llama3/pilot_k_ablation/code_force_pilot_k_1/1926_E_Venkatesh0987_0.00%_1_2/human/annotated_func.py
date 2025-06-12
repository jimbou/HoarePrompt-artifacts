#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * f
            print(y)
        else:
            print(2 * k - 1)
        
    #State: stdin is empty, t is 0, s is 0, i is 0, d is 0, h is 0, p is 1, g is 0, _ is t, n is undefined, k is undefined, f is undefined, y is undefined.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it calculates and prints the minimum number of operations required to reach a target value k, either by performing a series of operations that reduce n by half or by directly calculating the result if k is less than or equal to half of n. The function processes all test cases and leaves the input stream empty.

