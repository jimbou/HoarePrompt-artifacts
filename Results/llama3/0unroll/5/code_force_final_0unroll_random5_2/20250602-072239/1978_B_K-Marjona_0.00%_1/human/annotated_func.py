#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The sum of the minimum between n and b-a, and the sum of the minimum between n and b-a plus one, divided by two, multiplied by the minimum between n and b-a, plus the product of n minus the minimum between n and b-a and a, for each of the t test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers: n, a, and b. For each test case, it calculates and prints the minimum cost by either using the minimum of n and b-a consecutive numbers starting from b, or using a for the remaining numbers. The function processes all test cases and outputs the minimum cost for each case.

