#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: `_` is equal to the value of t, `x` is the last value of x, `n` is the last value of n, `k` is the last value of k, `ans` is the last value of ans, `i` is the integer division of the last value of x by the square root of the last value of x plus 2, and the maximum divisor of each x that is less than or equal to k has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers x and n. For each test case, it calculates the maximum divisor of x that is less than or equal to n and prints the result. The function processes all test cases and does not return any value.

