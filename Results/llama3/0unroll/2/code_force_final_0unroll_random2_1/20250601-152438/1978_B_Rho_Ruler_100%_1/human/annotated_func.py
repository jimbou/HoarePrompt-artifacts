#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b).
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns a value that is a combination of the products and differences of non-negative integers k, n, a, and b, where 0 <= k <= min(n, b). Specifically, it returns the product of k and b, minus the product of k and the integer division of (k-1) by 2, plus the product of (n-k) and a.

#Overall this is what the function does:Calculates a weighted sum of products involving non-negative integers k, n, a, and b, where k is within the range of 0 to the minimum of n and b, and returns the result.

#State of the program right berfore the function call: n, a, and b are positive integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: low is the smallest integer greater than or equal to n such that func_1(low, n, a, b) is the maximum value of func_1(mid, n, a, b) for all mid in the range [0, min(n, b)], high is low - 1, max_profit is the maximum value of func_1(mid, n, a, b) for all mid in the range [0, min(n, b)], n is unchanged, a is unchanged, b is unchanged.
    return max_profit
    #The program returns the maximum value of func_1(mid, n, a, b) for all mid in the range [0, min(n, b)].

#Overall this is what the function does:This function calculates and returns the maximum value of `func_1(mid, n, a, b)` for all `mid` in the range `[0, min(n, b)]`, where `n`, `a`, and `b` are positive integers. The function performs a binary search to find the maximum value, iteratively updating the search range and maximum profit until it converges to the optimal solution. The function does not modify the input variables `n`, `a`, or `b`.

