#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: The final output state after the loop executes all the iterations is that `x` is an integer greater than 1 and between 1 and 10^8, `n` is an integer between 1 and `x`, `k` is an integer equal to the integer division of `x` by `n`, `_` is equal to the number of times the loop has executed, `i` is the next odd number in the sequence (i.e., `i + 2`) after the last iteration of the loop, and `ans` is the maximum value in the list `l`. The list `l` contains the maximum value of the previous list `l`, `i`, and `x // i` if `x // i` is less than or equal to `k` and `i` is less than or equal to `k`. If `x` is not divisible by `i`, the state of `l` and `ans` remains unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers x and n. It calculates the maximum divisor of x that is less than or equal to x divided by n, and prints this value for each test case. If x is not divisible by any number less than or equal to x divided by n, it prints 1. The function processes all test cases and outputs the maximum divisor for each case.

