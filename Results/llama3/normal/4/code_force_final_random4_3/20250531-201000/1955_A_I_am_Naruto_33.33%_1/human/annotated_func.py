#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n > 1:
            ans1 = a * n
            ans2 = b * n // 2 + a * n % 2
            print(min(ans1, ans2))
        else:
            print(a)
        
    #State: `n` is an integer between 1 and 100, `a` is an integer between 1 and 30, `b` is an integer between 1 and 30, `_` is t-1, stdin is empty. If `n` is greater than 1, the minimum value between `a * n` and `b * n // 2 + a * n % 2` is printed. If `n` is equal to 1, the value of `a` is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains three integers (n, a, b). For each test case, it calculates and prints the minimum cost between two options: either paying a cost of 'a' for each of 'n' items or paying a cost of 'b' for every two items and 'a' for any remaining item. If 'n' is 1, it simply prints the cost 'a'. The function processes all test cases and leaves stdin empty.

