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
        
    #State: n is 0, m is the value of m after the last iteration, k is an integer equal to its original value minus the sum of all elements in L, L is a list that must have at least as many elements as the number of iterations, pow is 2 to the power of the number of iterations, tot is the sum of all elements in L, a is the last element in L, _ is t-1, t is greater than or equal to 0. If tot is less than k and k is less than or equal to tot plus a, then we break out of the most internal loop or if statement. Otherwise, no changes are made.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then performs a series of calculations involving these integers, including dividing n by 2 and updating k based on the results. The function prints the result of these calculations to standard output, specifically the value of 2^i * (2*k - 1), where i is the number of iterations and k is the updated value. The function repeats this process for each test case, reading input and printing output for each case.

