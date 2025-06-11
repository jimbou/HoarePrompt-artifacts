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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a sorted list of n positive integers, tickets_bought equals k, total_cost is the original total_cost plus the cost of k tickets at the prices of prices[0] to prices[i], i is the minimum of n-1 and the smallest integer such that tickets_bought equals k.
    return total_cost
    #The program returns the total cost of buying k tickets, where k is a positive integer less than or equal to the product of n and m, and the cost is calculated by adding the original total cost to the cost of k tickets at the prices of the first i tickets in the sorted list of n positive integers, where i is the minimum of n-1 and the smallest integer such that the number of tickets bought equals k.

#Overall this is what the function does:Functionality: This function calculates the minimum amount of money needed to purchase a specified number of tickets (k) over a certain number of days (n), with a daily limit on ticket purchases (m), given a list of prices per ticket for each day. It returns the total cost of buying k tickets at the lowest available prices, considering the daily purchase limit and the total number of tickets to buy.

#State of the program right berfore the function call: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, and prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: n is an integer, m is an integer, k is an integer such that k <= n*m, prices is a list of n positive integers, result is the output of func_1(n, m, k, prices), stdin contains 0 inputs, and t is greater than or equal to 1, and the result of func_1(n, m, k, prices) is printed

#Overall this is what the function does:Handles input and output for multiple test cases by reading the number of test cases, then for each test case, it reads three integers (n, m, k) and a list of n positive integers (prices), calls the func_1 function with these inputs, and prints the result.

