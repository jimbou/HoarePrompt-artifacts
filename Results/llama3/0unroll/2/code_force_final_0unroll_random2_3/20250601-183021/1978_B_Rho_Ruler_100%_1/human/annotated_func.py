#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9.
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns a value that is the result of the expression k * b - k * (k - 1) // 2 + (n - k) * a, where k, n, a, and b are integers such that 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9.

#Overall this is what the function does:Calculates and returns a value based on the input integers k, n, a, and b, representing a weighted sum of k and n-k, where k is bounded by the minimum of n and b, and n, a, and b are positive integers up to 10^9.

#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n, a, b <= 10^9
    low, high = 0, min(n, b)
    max_profit = 0
    while low <= high:
        mid = (low + high) // 2
        
        profit_mid = func_1(mid, n, a, b)
        
        profit_next = func_1(mid + 1, n, a, b)
        
        max_profit = max(max_profit, profit_mid)
        
        if profit_next > profit_mid:
            low = mid + 1
        else:
            high = mid - 1
        
    #State: low is the maximum value of mid such that func_1(mid, n, a, b) is maximum, high is low - 1, max_profit is the maximum value of func_1(mid, n, a, b) for all mid from 0 to the minimum of n and b.
    return max_profit
    #The program returns the maximum value of func_1(mid, n, a, b) for all mid from 0 to the minimum of n and b.

#Overall this is what the function does:This function calculates and returns the maximum value of `func_1(mid, n, a, b)` for all `mid` values ranging from 0 to the minimum of `n` and `b`. It iteratively adjusts the search range (`low` and `high`) to find the maximum value, utilizing a binary search approach. The function takes four parameters: `n`, `a`, `b`, and returns the maximum profit value.

