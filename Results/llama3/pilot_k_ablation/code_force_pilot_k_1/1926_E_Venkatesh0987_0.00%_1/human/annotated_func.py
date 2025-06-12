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
        
    #State: stdin is empty, t is 0, n and k are the last two integers in the input, s is 0, i is 0, d is an integer equal to the last n, h is an integer equal to the last n, p is 1, g is 0, _ is t. If t is 0, then the values of n, k, s, i, d, h, p, and g are undefined.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it calculates and prints the result of a specific operation based on the values of n and k. If k is greater than half of n, it performs a series of calculations involving divisions and multiplications, and prints the final result. If k is not greater than half of n, it simply prints 2 times k minus 1. After processing all test cases, the function leaves the input stream empty and the variables n, k, and other internal variables in an undefined state.

