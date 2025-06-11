#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: t is 0, n is 0, k is an integer between 1 and 0 inclusive, L is an empty list, tot is equal to the sum of all elements in the list, pow is 2 to the power of the number of elements in the list, stdin is empty, a is undefined.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then generates a sequence of integers by repeatedly subtracting the largest possible integer from n until n becomes 0. For each test case, it iterates through the generated sequence and checks if the cumulative sum of the sequence elements is within the range [k, k + a], where a is the current sequence element. If it is, the function prints the result of the expression 2 * (k - tot) - 1 multiplied by 2 to the power of the number of elements in the sequence. The function repeats this process for all test cases and leaves the input stream empty.

