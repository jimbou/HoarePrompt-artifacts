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
        
    #State: stdin is empty, n is not defined, k is not defined, s is not defined, i is not defined, d is not defined, h is not defined, p is not defined, g is not defined, _ is equal to t, f is not defined, y is not defined, and t lines have been printed, each containing an integer.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it calculates and prints an integer value based on the values of n and k. If k is greater than half of n, it performs a series of calculations involving divisions and multiplications to determine the output value. If k is less than or equal to half of n, it simply prints 2 times k minus 1. The function continues this process until all test cases have been read from standard input, at which point the input is empty and the function has printed one integer value for each test case.

