#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two positive integers n and m, such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: ans is equal to n plus the sum of (n + i) integer divided by i squared for i from 2 to the square root of n plus 1, k is a positive integer, n is a positive integer, root is an integer equal to the square root of n plus 1, stdin contains multiple test cases minus one.
    print(ans)
    #This is printed: n + sum of (n + i) / i^2 for i from 2 to sqrt(n) + 1 (where n is a positive integer)

#Overall this is what the function does:Calculates and prints the sum of a positive integer n and the sum of (n + i) integer divided by i squared for i from 2 to the square root of n plus 1, given n and another positive integer k as input, and then consumes the next test case from standard input.

