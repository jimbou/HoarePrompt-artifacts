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
        
    #State: n is a positive integer, m is a positive integer, k is a positive integer such that k <= n*m, prices is a sorted list of n positive integers, total_cost is the cost of k tickets at the lowest prices in the list, tickets_bought is k, i is the index of the last price used to buy tickets or n-1 if all prices were used.
    return total_cost
    #The program returns the total cost of k tickets at the lowest prices in the sorted list 'prices' of n positive integers.

#Overall this is what the function does:Functionality: This function calculates the minimum amount of money needed to purchase a specified number of tickets (k) given a list of daily ticket prices (prices) and a maximum number of tickets that can be bought each day (m). It sorts the prices in ascending order and then iteratively buys the maximum allowable tickets (m) at the lowest available price until it reaches the target number of tickets (k). The function returns the total cost of the purchased tickets.

#State of the program right berfore the function call: n, m, and k are positive integers, prices is a list of n positive integers.
    """Handles input and output for multiple test cases."""
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        prices = list(map(int, input().split()))
        
        result = func_1(n, m, k, prices)
        
        print(result)
        
    #State: n, m, and k are positive integers, prices is a list of n positive integers, result is the output of func_1(n, m, k, prices), stdin contains 0 inputs, _ is t-1, and the result of func_1(n, m, k, prices) has been printed t times.

#Overall this is what the function does:Handles input and output for multiple test cases by reading the number of test cases, then for each test case, it reads three positive integers (n, m, k) and a list of n positive integers (prices), calls the func_1 function with these inputs, and prints the result. After all test cases have been processed, the function concludes with the results of func_1 printed for each test case.

