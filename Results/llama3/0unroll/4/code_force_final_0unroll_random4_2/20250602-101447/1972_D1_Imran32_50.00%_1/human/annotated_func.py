#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6). The number of test cases t (1 <= t <= 10^4) is given on the first line.
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: ans is equal to n plus the sum of (n + i) // (i * i) for all i from 2 to the square root of n plus 1, root is equal to the square root of n plus 1, n is a positive integer, k is a positive integer, stdin contains multiple test cases minus one.
    print(ans)
    #This is printed: n + sum of (n + i) // (i * i) for all i from 2 to the square root of n plus 1

#Overall this is what the function does:Calculates and prints the sum of the number of factors for a given positive integer n, where the number of factors is calculated as n plus the sum of (n + i) // (i * i) for all i from 2 to the square root of n plus 1, and then moves on to the next test case.

