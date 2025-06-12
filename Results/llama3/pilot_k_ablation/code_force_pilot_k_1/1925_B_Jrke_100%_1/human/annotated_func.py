#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 ≤ t ≤ 10^3) and the rest t inputs are two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
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
        
    #State: stdin contains no input, `t` is an integer between 1 and 10^3, `x` and `n` are integers between 1 and 10^8, `k` is an integer equal to the integer division of `x` by `n`, `ans` is the maximum divisor of `x` that is less than or equal to `k` for each of the `t` inputs.

#Overall this is what the function does:This function reads a series of inputs from stdin, where the first input is the number of test cases (t), followed by t pairs of integers (x and n). For each pair, it calculates the maximum divisor of x that is less than or equal to the integer division of x by n (k), and prints this value. The function processes all test cases and does not return any value, leaving stdin empty after execution.

