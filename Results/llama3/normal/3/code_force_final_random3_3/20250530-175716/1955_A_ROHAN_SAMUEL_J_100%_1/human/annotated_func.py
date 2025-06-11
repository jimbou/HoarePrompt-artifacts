#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains three integers n, a, and b (1 ≤ n ≤ 100, 1 ≤ a, b ≤ 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: The loop has executed for a number of times equal to the value of the variable `t` read from the first line of stdin. `n`, `a`, and `b` are integers between 1 and 100, 1 and 30, and 1 and 30 respectively, stdin contains `t` lines of input that contain three integers `n`, `a`, and `b`. If `n` is odd, if 2 times `a` is less than `b`, the product of `a` and `n` is printed. Otherwise, the product of half of `n` and `b` added to `a` is printed. If `n` is even, if 2 times `a` is less than `b`, the product of `a` and `n` is being printed. Otherwise, the value of `n` divided by 2 times `b` is being printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains three integers n, a, and b. For each test case, it calculates and prints the minimum cost based on the values of n, a, and b, considering whether n is odd or even and the relationship between 2a and b. The function processes all test cases and prints the corresponding minimum costs.

