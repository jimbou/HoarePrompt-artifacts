#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(read_input())
    #The program returns an integer greater than 0 that was provided as input.

#Overall this is what the function does:Reads an integer greater than 0 from standard input and returns it as an integer.

#State of the program right berfore the function call: read_input() returns a string containing a space-separated list of integers.
    return map(int, read_input().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a string from the space-separated list of integers returned by read_input() to an integer.

#Overall this is what the function does:Converts a space-separated list of integers from user input into a sequence of integers.

#State of the program right berfore the function call: primary_items is a list of pairs of integers, secondary_heap is a list of pairs of integers, and the pairs in both lists represent the prices of items for Alice and Bob respectively.
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: `primary_items` is an empty list, `secondary_heap` is a list of pairs of integers, `total` is the sum of the first elements of the pairs in `secondary_heap` plus the sum of the elements of all items in `primary_items` that had a sum greater than or equal to 0.
    return total
    #The program returns the sum of the first elements of the pairs in `secondary_heap` plus the sum of the elements of all items in `primary_items` that had a sum greater than or equal to 0. Since `primary_items` is an empty list, the sum of its elements is 0, so the program returns the sum of the first elements of the pairs in `secondary_heap`.

#Overall this is what the function does:This function calculates the total sum of prices for Alice and Bob. It takes a list of pairs of integers representing prices for Alice and Bob, and returns the sum of the first elements of the pairs in Bob's list plus the sum of the elements of all items in Alice's list that had a sum greater than or equal to 0. The function modifies Alice's list by emptying it.

#State of the program right berfore the function call: test_cases is a positive integer
    test_cases = func_1()
    for _ in range(test_cases):
        heap = []
        
        remaining_items = []
        
        n, k = func_2()
        
        prices = list(func_2())
        
        neg_prices = [(-price) for price in prices]
        
        bonuses = list(func_2())
        
        max_profit = 0
        
        current_profit = 0
        
        combined = list(zip(neg_prices, bonuses))
        
        combined.sort(key=lambda item: item[1])
        
        for _ in range(k):
            if combined:
                heapq.heappush(heap, combined.pop())
        
        if combined:
            current_profit = func_3(combined, heap)
        
        if current_profit > max_profit:
            max_profit = current_profit
        
        while combined:
            item = combined.pop()
            if item[0] + item[1] >= 0:
                current_profit -= item[1]
            else:
                current_profit += item[0]
            removed_item = heapq.heappushpop(heap, item)
            if removed_item:
                current_profit -= removed_item[0]
            if current_profit > max_profit:
                max_profit = current_profit
        
        print(max_profit)
        
    #State: `test_cases` is greater than 0, `_` is equal to `test_cases`, `n` and `k` are the return values of `func_2()`, `prices` is a list of values returned by `func_2()`, `neg_prices` is a list of negative values of `prices`, `bonuses` is a list of values returned by `func_2()`, `heap` is empty, `item` is undefined, `combined` is empty, `remaining_items` is empty, and `max_profit` is the maximum profit that can be obtained by buying and selling items with the given prices and bonuses.

#Overall this is what the function does:This function determines the maximum profit that can be obtained by buying and selling items with given prices and bonuses. It accepts no parameters and returns no value, but instead prints the maximum profit for each test case. The function iterates over a number of test cases, and for each test case, it generates a list of prices and bonuses, sorts them based on the bonuses, and then simulates a process of buying and selling items to maximize the profit. The function uses a heap data structure to keep track of the items with the highest bonuses and updates the maximum profit as it processes the items.

