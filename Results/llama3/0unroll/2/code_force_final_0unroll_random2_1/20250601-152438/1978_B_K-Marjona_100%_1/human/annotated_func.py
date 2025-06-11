#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The output state is the sum of the products of the minimum of n and b-a, and b, minus the sum of the products of the minimum of n and b-a, and the minimum of n and b-a minus one, divided by two, plus the product of n minus the minimum of n and b-a, and a.

#Overall this is what the function does:Calculates and prints the maximum sum of products for multiple test cases, where each test case consists of three integers n, a, and b. For each test case, it determines the minimum of n and b-a, and then calculates the sum of products based on this minimum value and the values of a and b. If b is less than or equal to a, it simply prints the product of a and n. Otherwise, it prints the calculated sum of products.

