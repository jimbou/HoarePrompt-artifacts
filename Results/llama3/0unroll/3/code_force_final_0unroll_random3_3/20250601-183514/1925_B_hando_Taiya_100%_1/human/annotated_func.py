#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^3), then t pairs of integers x and n (1 <= x <= 10^8 and 1 <= n <= x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: The largest divisor of x that is less than or equal to n.
    print(ans)
    #This is printed: the largest divisor of x that is less than or equal to n

#Overall this is what the function does:This function takes two integers x and n as input and returns the largest divisor of x that is less than or equal to n. It reads input from stdin, where the first input is an integer t (1 <= t <= 10^3) representing the number of test cases, followed by t pairs of integers x and n (1 <= x <= 10^8 and 1 <= n <= x). The function iterates through all divisors of x, updates the maximum divisor that is less than or equal to n, and prints the result.

