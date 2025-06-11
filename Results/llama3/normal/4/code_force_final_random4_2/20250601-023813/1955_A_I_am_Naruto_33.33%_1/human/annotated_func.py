#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `_` is t-1, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers: n, a, and b. For each test case, it calculates and prints the minimum cost between two options: either buying 'n' items at price 'a' each, or buying 'n' items at price 'b' each but with a constraint that 'b' is only applicable for even quantities (rounded down to the nearest whole number), with the remainder (if any) being purchased at price 'a'. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

