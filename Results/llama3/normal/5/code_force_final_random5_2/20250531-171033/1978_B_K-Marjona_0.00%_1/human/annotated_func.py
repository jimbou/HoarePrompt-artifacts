#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: n is an integer between 1 and 10^9, a is an integer between 1 and 10^9, b is an integer between 1 and 10^9, k is an integer equal to the minimum of n and b - a, stdin is empty. If b is less than or equal to a, the product of a and n is printed. Otherwise, the sum of the first k terms of the arithmetic sequence starting from b - k + 1 with a common difference of 1 is printed, plus the product of the remaining n - k terms and a.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the total cost for each case. For each test case, it calculates the cost based on the given integers n, a, and b. If b is less than or equal to a, it prints the product of a and n. Otherwise, it calculates the sum of the first k terms of an arithmetic sequence starting from b - k + 1 with a common difference of 1, plus the product of the remaining n - k terms and a, and prints the result. The function continues this process until all test cases have been processed, leaving stdin empty.

