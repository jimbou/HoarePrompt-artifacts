#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4), then t pairs of integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: n and k are integers, s is 0, i is 0, d is n, h is n, p is 1, g is 0. If k > (n + 1) // 2, then s is greater than or equal to k or d is 0, i is greater than or equal to 1, d is greater than or equal to 0, h is less than or equal to -i+1, p is i, g is greater than or equal to (n+1)//2 + (h+1)//2 + (h+1)//2 + ... + (h+1)//2 (i-1 times), f is k minus g, y is 2 to the power of i minus 1, times f, and y is printed, where y is equal to 2 to the power of i minus 1, times f. If k <= (n + 1) // 2, then 2 times k minus 1 is printed.

#Overall this is what the function does:This function reads input from stdin, where the first input is an integer t, representing the number of test cases. For each test case, it reads two integers n and k. If k is greater than half of n, it calculates a value y based on a series of operations involving n and k, and prints y. If k is less than or equal to half of n, it simply prints 2 times k minus 1. The function repeats this process for all t test cases.

