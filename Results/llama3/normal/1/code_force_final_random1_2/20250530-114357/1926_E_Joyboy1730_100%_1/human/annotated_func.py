#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 5 * 10^4), and each of the remaining t inputs is a pair of integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: t is 0, n is 0, k is an integer (1 <= k <= n), _ is t, L is an empty list, stdin is empty, tot is the sum of all elements in L, pow is 2 to the power of the number of elements in L. If tot is less than k and k is less than or equal to the sum of tot and the last element in L, then the result of the expression 2 to the power of the number of elements in L minus 1, multiplied by 2 times k minus tot minus 1, is printed.

#Overall this is what the function does:The function reads a series of inputs from stdin, where the first input is an integer t representing the number of test cases, and each subsequent input is a pair of integers n and k. For each test case, it generates a sequence of integers L by repeatedly subtracting the largest possible integer m from n, such that n - m is non-negative, and appending m to L. It then iterates through L, keeping track of the cumulative sum tot and the power of 2 pow. If the cumulative sum tot is less than k and k is less than or equal to the sum of tot and the current element in L, it prints the result of the expression 2 to the power of the number of elements in L minus 1, multiplied by 2 times k minus tot minus 1. After processing all test cases, the function leaves the input stream empty and the variables t, n, k, and L in a final state.

