#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and x - n * (x // i) % (x // i
                    ) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: stdin is empty, x is not defined, n is not defined, ans is not defined, q is equal to t, and t lines of output have been printed, each containing the maximum divisor of the corresponding x such that x - n * divisor is divisible by divisor.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers x and n. For each test case, it calculates and prints the maximum divisor of x such that x minus n times the divisor is divisible by the divisor. The function processes all test cases and produces the corresponding output, leaving the standard input empty.

