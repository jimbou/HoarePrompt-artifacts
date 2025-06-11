#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: t is a positive integer greater than or equal to 1 and less than or equal to 10^4, n is an integer greater than or equal to 1 and less than or equal to 10^9, a is an integer greater than or equal to 1 and less than or equal to 10^9, b is an integer greater than or equal to 1 and less than or equal to 10^9, k is an integer greater than or equal to 0 and less than or equal to 10^9, _ is t - 1, stdin contains 0 lines of input. If b is less than or equal to a, the product of a and n is printed. Otherwise, the expression b * k - k * (k - 1) // 2 + (n - k) * a is printed.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains a positive integer t (1 <= t <= 10^4) and each subsequent line contains three integers n, a, and b (1 <= n, a, b <= 10^9). For each set of n, a, and b, it calculates and prints the minimum cost based on the condition that if b is less than or equal to a, it prints the product of a and n; otherwise, it prints the result of the expression b * k - k * (k - 1) // 2 + (n - k) * a, where k is the minimum of n and b - a. After processing all input lines, the function concludes, leaving the standard input empty.

