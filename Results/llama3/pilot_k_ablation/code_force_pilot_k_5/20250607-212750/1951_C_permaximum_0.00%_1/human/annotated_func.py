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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a sorted list of n positive integers, total_cost is the sum of the cost of all tickets bought, tickets_bought is equal to k, i is the number of iterations it took to buy k tickets, tickets_to_buy is 0, cost is the cost of the tickets bought in the last iteration.
    return total_cost
    #The program returns the total cost of all tickets bought, which is the sum of the cost of k tickets, where k is a positive integer less than or equal to the product of the number of positive integers in the prices list and a positive integer m.

#Overall this is what the function does:Calculates the minimum cost to purchase a specified number of tickets within a given budget constraint, considering daily ticket purchase limits and varying ticket prices across different days, and returns the total minimum cost incurred to buy the required number of tickets.

#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, and prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: t is 0, _ is t, n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a list of n positive integers, result is the return value of func_1(n, m, k, prices), stdin contains no inputs, and the result of func_1(n, m, k, prices) is printed t times.

#Overall this is what the function does:This function reads input for multiple test cases, where each test case consists of three positive integers (n, m, k) and a list of n positive integers (prices), and then prints the result of calling the func_1 function with these inputs, repeating this process t times.

