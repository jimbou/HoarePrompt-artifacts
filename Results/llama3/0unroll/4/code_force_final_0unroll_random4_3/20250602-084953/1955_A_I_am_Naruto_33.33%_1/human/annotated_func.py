#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the minimum of two values: the product of n and a, and the product of n and b divided by 2, plus the remainder of the division of n and a by 2. If n is 1, the integer on that line will be a.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers: n, a, and b. For each case, it calculates and prints the minimum of two values: the product of n and a, and the product of n and b divided by 2, plus the remainder of the division of n and a by 2. If n is 1, it simply prints the value of a. The function processes all test cases and outputs the results, one per line.

