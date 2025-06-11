#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, and prices is a list of n positive integers.
    """Calculates the minimum spending to purchase k tickets.

    Args:
        n: The number of sale days.
        m: The maximum number of tickets purchasable each day.
        k: The total number of tickets to buy.
        prices: A list of prices per ticket for each day.

    Returns:
        The minimum amount of money needed to purchase k tickets.
    """
    total_cost = 0
    tickets_bought = 0
    prices.sort()
    for i in range(n):
        tickets_to_buy = min(m, k - tickets_bought)
        
        cost = tickets_to_buy * prices[i]
        
        total_cost += cost
        
        tickets_bought += tickets_to_buy
        
        if tickets_bought == k:
            break
        
    #State: Output State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a sorted list of n positive integers, total_cost is the total cost of the tickets bought, tickets_bought is k.
    return total_cost
    #The program returns the total cost of k tickets, where k is a positive integer less than or equal to the product of the number of positive integers in the sorted list 'prices' and a positive integer m, and the total cost is the sum of the costs of the tickets bought.

#Overall this is what the function does:Calculates the minimum cost to purchase a specified number of tickets by buying the cheapest tickets first, up to a maximum number of tickets per day, and returns the total cost of the purchased tickets.

#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= min(n*m, 10^9), and prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: t is a positive integer, n is a positive integer, m is a positive integer, k is a positive integer such that k <= min(n*m, 10^9), prices is a list of n positive integers, stdin is empty

#Overall this is what the function does:Handles input and output for multiple test cases, reading the number of test cases, then for each test case, reads three positive integers (n, m, k) and a list of n positive integers (prices), calls func_1 with these inputs, and prints the result.

