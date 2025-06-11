#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The output state will be the sum of the products of the minimum of n and b-a, and b, minus the sum of the products of the minimum of n and b-a, and the minimum of n and b-a minus one, divided by two, plus the product of n minus the minimum of n and b-a, and a, for each test case.

#Overall this is what the function does:Calculates and prints the maximum sum of products for each test case, considering the minimum of n and b-a, and either b or a, depending on whether b is greater than a or not.

