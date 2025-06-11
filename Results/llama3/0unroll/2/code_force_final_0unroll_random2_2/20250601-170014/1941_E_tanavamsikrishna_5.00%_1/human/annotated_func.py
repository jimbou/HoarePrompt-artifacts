#State of the program right berfore the function call: row is a list of non-negative integers, d is a positive integer such that d <= len(row).
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: The first d-1 elements of the list row have been incremented by 1, while the rest of the elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: The first d-1 elements of the list row have been incremented by 1, while the rest of the elements have been updated to be the sum of the minimum value of the previous d+1 elements and the original value plus 1.
    return row[-1]
    #The program returns the last element of the list row, which is the sum of the minimum value of the previous d+1 elements and the original value plus 1.

#Overall this is what the function does:This function takes a list of non-negative integers and a positive integer as input, increments the first d-1 elements by 1, updates the rest of the elements to be the sum of the minimum value of the previous d+1 elements and the original value plus 1, and returns the last element of the updated list.

#State of the program right berfore the function call: n, m, k, and d are positive integers, n is the number of rows, m is the number of columns, k is the number of bridges, and d is the maximum distance between supports. rows is a 2D list of non-negative integers representing the depths of the river cells.
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: The total_costs list contains the sum of every k consecutive elements in the costs list, starting from the first element up to the (len(costs) - k + 1)th element.
    print(min(total_costs))
    #This is printed: the minimum sum of k consecutive elements in the costs list

#Overall this is what the function does:This function calculates the minimum sum of k consecutive elements in a list of costs, where each cost represents the total cost of building a bridge across a river with a given maximum distance between supports. The function takes as input the number of rows, columns, bridges, and maximum distance, as well as a 2D list of river depths, and returns the minimum sum of k consecutive costs.

