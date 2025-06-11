#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: The output state will contain t lines, each containing a single integer, which is the result of the calculation for the corresponding input values of n and k. The integer will be the product of a power of 2 and an odd number (2*k - 1), where k is the input value of k.

#Overall this is what the function does:This function reads a series of input values from standard input, where each input set consists of two integers, n and k. It then performs a calculation based on these values, producing a result that is the product of a power of 2 and an odd number (2*k - 1). The function outputs this result for each input set, with the output being a series of integers, one for each input set.

