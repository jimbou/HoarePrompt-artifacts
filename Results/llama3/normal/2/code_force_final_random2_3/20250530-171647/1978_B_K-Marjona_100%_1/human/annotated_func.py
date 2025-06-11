#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: n is an integer greater than or equal to 0, a is an integer, b is an integer, k is an integer, _ is equal to the number of test cases in stdin, stdin is empty, n, a, and b are assigned the last set of integer values from stdin, k is assigned the minimum value between n and b - a. If b is less than or equal to a, the product of a and n is printed. Otherwise, the value of b * k - k * (k - 1) // 2 + (n - k) * a is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains three integers: the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price. It calculates and prints the total cost of the buns based on the given prices, considering the minimum number of buns that can be sold at the modified price. If the modified price is less than or equal to the usual price, it simply prints the product of the usual price and the number of buns. Otherwise, it calculates the total cost by adding the cost of the buns sold at the modified price and the cost of the remaining buns sold at the usual price. The function continues processing test cases until all input has been read, leaving the standard input empty.

