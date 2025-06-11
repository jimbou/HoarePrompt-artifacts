#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: The output state will be the maximum possible value of 'ans' for each test case, which is the maximum divisor of 'x' that can divide 'x' minus 'n' times the divisor, and the result is non-negative and divisible by the divisor. The output will be the maximum of these values for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, x and n. For each test case, it calculates and prints the maximum divisor of x that can divide x minus n times the divisor, resulting in a non-negative and divisible value. The function iterates through all possible divisors of x, checks the conditions, and updates the maximum divisor if a larger one is found. The function outputs the maximum possible value of the divisor for each test case.

