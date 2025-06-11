#State of the program right berfore the function call: row is a list of non-negative integers, d is a positive integer such that d <= len(row).
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: The first d-1 elements of the list row have been incremented by 1, while the remaining elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: The first d-1 elements of the list row have been incremented by 1, and the remaining elements have been updated to be the sum of the minimum value of the previous d+1 elements (or 0 if i is 0) and the original value of the element plus 1.
    return row[-1]
    #The program returns the last element of the list row, which is the sum of the minimum value of the previous d+1 elements (or 0 if i is 0) and the original value of the element plus 1.

#Overall this is what the function does:This function modifies a list of non-negative integers by incrementing the first d-1 elements by 1 and updating the remaining elements to be the sum of the minimum value of the previous d+1 elements (or 0 if the element is the first) and the original value of the element plus 1. The function then returns the last element of the modified list.

#State of the program right berfore the function call: n, m, k, and d are positive integers, n is the number of rows, m is the number of columns, k is the number of bridges, and d is the maximum distance between supports. rows is a list of lists of non-negative integers representing the depths of the river cells.
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: n, m, k, and d are positive integers, rows is a 2D list of non-negative integers, costs is a list of results from func_1 applied to each row in rows with d as an argument, total_costs is a list of sums of sublists of costs of length k, stdin is empty.
    print(min(total_costs))
    #This is printed: minimum sum of k consecutive elements in the costs list (where costs is a list of results from func_1 applied to each row in rows with d as an argument)

#Overall this is what the function does:Calculates and prints the minimum sum of k consecutive elements in the costs list, where costs is a list of results from func_1 applied to each row in the input 2D list rows with d as an argument.

