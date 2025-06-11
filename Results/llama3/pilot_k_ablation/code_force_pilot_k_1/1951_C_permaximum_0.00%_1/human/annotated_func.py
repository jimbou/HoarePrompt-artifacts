#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n * m, and prices is a list of n positive integers.
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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n * m, prices is a sorted list of n positive integers, total_cost is the total cost of k tickets, tickets_bought is k, i is the index of the last ticket bought, tickets_to_buy is 0, cost is the cost of the last tickets_to_buy. If k is less than or equal to m, then the loop executes only once. If k is greater than m, then the loop executes until tickets_bought equals k. If k is 0, then the loop does not execute and total_cost and tickets_bought are 0.
    return total_cost
    #The program returns the total cost of k tickets, where k is a positive integer less than or equal to the product of n and m, and the tickets are bought from a sorted list of n positive integers.

#Overall this is what the function does:Calculates the minimum cost to purchase a specified number of tickets from a list of daily prices, considering a limit on the number of tickets that can be bought each day, and returns the total cost.

#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= min(n*m, 10^9), and prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= min(n*m, 10^9), prices is a list of n positive integers, t is 0, _ is t, stdin contains no input, and the result (which is the return value of func_1(n, m, k, prices)) has been printed t times.

#Overall this is what the function does:Handles input and output for multiple test cases by reading the number of test cases, processing each case by reading input parameters (n, m, k, and prices), calling a function (func_1) with these parameters, and printing the result for each case, until all test cases have been processed and no input is left in stdin.

