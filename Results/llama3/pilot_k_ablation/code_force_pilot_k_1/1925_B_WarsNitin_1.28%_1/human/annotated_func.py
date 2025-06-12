#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
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
        
    #State: stdin is empty, q is equal to the initial value of t, ans is not defined, x and n are not defined, the maximum divisor i of x such that x - n * i is divisible by i or x - n * (x // i) is divisible by x // i, if such a divisor exists, otherwise 1, has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers x and n. For each case, it calculates and prints the maximum divisor i of x such that x - n * i is divisible by i or x - n * (x // i) is divisible by x // i. If no such divisor exists, it prints 1. The function processes all test cases and then terminates, leaving the standard input empty.

