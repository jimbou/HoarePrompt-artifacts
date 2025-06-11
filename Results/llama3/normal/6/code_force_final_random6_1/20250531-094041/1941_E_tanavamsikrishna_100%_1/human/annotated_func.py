#State of the program right berfore the function call: row is a list of non-negative integers, d is a positive integer such that d < len(row).
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list of non-negative integers where the first element is 1 and each subsequent element is increased by 2 times its index, `d` is a positive integer such that `d` is equal to `len(row) - 1`, `i` is `d - 1`.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: row is a list of non-negative integers where the first element is 1 and each subsequent element is increased by 2 times its index, except for the elements at indices d, d+1, ..., len(row)-1 which are now e[0] + row[i] + 1, d is a positive integer such that d is equal to len(row) - 1, i is equal to len(row) - 1, min_heap is a list of tuples where each tuple contains an element from row[:d] and its index, and min_heap is a valid min heap with no elements having an index less than or equal to len(row) - (d + 2), except for the newly added tuples (row[i], i) and the tuple e.
    return row[-1]
    #The program returns the last element of the list 'row', which is e[0] + row[i] + 1, where e[0] is an unknown value, i is equal to len(row) - 1, and row[i] is a non-negative integer that was increased by 2 times its index.

#Overall this is what the function does:The function modifies the input list 'row' by first setting the first element to 1 and incrementing each subsequent element by 2 times its index, up to the 'd'th element. It then creates a min heap from the first 'd' elements of 'row' and iteratively updates the remaining elements of 'row' by adding 1 to the sum of the current element and the smallest element from the heap that is not outdated (i.e., its index is not less than or equal to the current index minus 'd' plus 2). The function returns the last element of the modified list 'row'.

#State of the program right berfore the function call: n, m, k, and d are positive integers, rows is a list of lists of non-negative integers, and d is less than or equal to m.
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: n, m, k, and d are positive integers, rows is a list of lists of non-negative integers, costs is a list of integers, total_costs is a list containing the sum of every k integers in costs, stdin contains no input, i is len(costs) - (k - 1)
    print(min(total_costs))
    #This is printed: the minimum sum of k consecutive integers in the costs list

#Overall this is what the function does:Calculates and prints the minimum sum of k consecutive integers in a list of costs, which are derived from a 2D list of non-negative integers (rows) and a positive integer (d).

