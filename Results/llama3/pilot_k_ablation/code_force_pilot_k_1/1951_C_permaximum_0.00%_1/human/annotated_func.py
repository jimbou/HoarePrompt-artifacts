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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a sorted list of n positive integers, total_cost is the total cost of k tickets, tickets_bought is k.
    return total_cost
    #The program returns the total cost of k tickets, where k is a positive integer less than or equal to the product of n and m, and the cost is calculated from a sorted list of n positive integers representing prices.

#Overall this is what the function does:Functionality: This function calculates the minimum amount of money needed to purchase a specified number of tickets, given a list of prices per ticket for each day and the maximum number of tickets that can be bought each day. It takes four parameters: the number of sale days, the maximum number of tickets purchasable each day, the total number of tickets to buy, and a list of prices per ticket for each day. The function returns the total cost of the tickets, which is the minimum amount of money needed to purchase the specified number of tickets. The function sorts the prices in ascending order and then iterates over the sorted prices, buying as many tickets as possible each day until the total number of tickets to buy is reached. The function returns the total cost of the tickets, which is the sum of the costs of all the tickets bought.

#State of the program right berfore the function call: t is a positive integer, n, m, and k are positive integers, prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: t is 0, stdin is empty, n, m, and k are the last values read from stdin, prices is the last list of prices read from stdin, result is the last output of func_1(n, m, k, prices).

#Overall this is what the function does:Reads input for multiple test cases, where each case consists of three positive integers (n, m, k) and a list of n positive integers (prices), processes each case using the func_1 function, and prints the result of each case. The function consumes all input from stdin and leaves it empty.

