#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The output state will be the sum of the products of the minimum of n and b-a, and the average of b and b-k+1, plus the product of n-k and a, for each iteration of the loop.

#Overall this is what the function does:This function calculates and prints the total cost for a series of transactions, where each transaction involves purchasing a certain quantity of items at a specified price. The function takes no arguments and reads input from standard input, expecting a specific format. It processes each transaction by determining the minimum quantity that can be purchased at a discounted price and calculates the total cost accordingly. The function prints the total cost for each transaction.

