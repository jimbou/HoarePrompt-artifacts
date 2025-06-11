#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 5 * 10^4), and the remaining t inputs are two space-separated integers n and k (1 <= k <= n <= 10^9).
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
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: t is an integer greater than or equal to 0, n is an integer between 1 and 10^9, k is an integer between 1 and n, _ is t, s is 0, i is 0, d is n, h is n, p is 1, g is 0.

#Overall this is what the function does:This function calculates and prints the minimum number of operations required to reach a target number k from n, where the operation involves either adding or subtracting the largest possible power of 2 that does not exceed the current number. The function takes t sets of inputs, where each set contains two integers n and k, and prints the result for each set. If k is greater than half of n, the function performs a series of calculations involving powers of 2 and subtractions to determine the minimum number of operations. If k is less than or equal to half of n, the function simply prints 2 times k minus 1.

