#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4) and then t pairs of integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: t is 0, n is 0, k is an integer between 1 and 10^9 inclusive, L is an empty list, tot is 0, pow is 1.

#Overall this is what the function does:The function reads a series of inputs from stdin, where the first input is an integer t, representing the number of test cases, followed by t pairs of integers n and k. For each pair, it calculates a value based on the binary representation of n and prints the result if k falls within a certain range. The function iterates through all test cases, performing the calculation and printing results as applicable, and concludes with all input variables reset to their initial state.

