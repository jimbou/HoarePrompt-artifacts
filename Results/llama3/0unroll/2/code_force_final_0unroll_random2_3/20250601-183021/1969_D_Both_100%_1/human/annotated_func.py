#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(read_input())
    #The program returns an integer greater than 0 that was provided as input.

#Overall this is what the function does:Reads an integer greater than 0 from standard input and returns it as an integer.

#State of the program right berfore the function call: read_input() returns a string containing space-separated integers.
    return map(int, read_input().split())
    #The program returns a map object that contains integers converted from the space-separated integers in the string returned by read_input()

#Overall this is what the function does:Converts a string of space-separated integers into a map object containing integers.

#State of the program right berfore the function call: primary_items is a list of pairs of integers, secondary_heap is a list of pairs of integers, and for each pair of integers (x, y), x and y are non-negative integers.
    total = sum(item[0] for item in secondary_heap)
    for item in primary_items:
        if item[0] + item[1] >= 0:
            total += item[0] + item[1]
        
    #State: Output State: `primary_items` is a list of pairs of integers, `secondary_heap` is a list of pairs of integers, and for each pair of integers (x, y), x and y are non-negative integers, `total` is the sum of the first elements of all pairs in `secondary_heap` plus the sum of the elements of all pairs in `primary_items` where the sum of the pair is non-negative.
    return total
    #The program returns the sum of the first elements of all pairs in `secondary_heap` plus the sum of the elements of all pairs in `primary_items` where the sum of the pair is non-negative.

#Overall this is what the function does:This function calculates the total sum of specific pairs of integers from two lists, `primary_items` and `secondary_heap`. It sums the first elements of all pairs in `secondary_heap` and adds the sums of pairs from `primary_items` where both integers in a pair are non-negative. The function returns this total sum without modifying the input lists.

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
        
    #State: The loop has executed `test_cases` number of times, and for each execution, it has calculated and printed the maximum profit that can be achieved by selecting `k` items from the `combined` list, considering their prices and bonuses. The state of the variables outside the loop remains unchanged.

#Overall this is what the function does:Calculates and prints the maximum profit that can be achieved by selecting k items from a list of combined prices and bonuses, considering the optimal selection of items to maximize profit, and repeats this process for a specified number of test cases.

