#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6).
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: n is a positive integer greater than 1, k is a positive integer, ans is equal to n plus the sum of (n + i) divided by i squared for i from 2 to the square root of n plus 1, root is equal to the square root of n plus 1, i is equal to the square root of n plus 1, stdin contains multiple test cases minus one.
    print(ans)
    #This is printed: n + sum((n + i) / i^2 for i in range(2, sqrt_n_plus_1 + 1)) (where n is a positive integer greater than 1 and sqrt_n_plus_1 is the square root of n plus 1)

#Overall this is what the function does:Calculates and prints the sum of a series of numbers based on the input values n and k, where n is a positive integer greater than 1 and k is a positive integer. The function takes no arguments and reads input from stdin. It calculates the sum of (n + i) divided by i squared for i from 2 to the square root of n plus 1, adds this sum to n, and prints the result. The function does not modify the input values or have any side effects other than printing the result.

