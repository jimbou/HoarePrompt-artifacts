#State of the program right berfore the function call: n is a non-negative integer, operations is a list of tuples where each tuple contains two integers, the first integer is either 1 or 2, and the second integer is a non-negative integer, and queries is a list of non-negative integers.
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: Output State: n is a non-negative integer, operations is an empty list, queries is a list of non-negative integers, array is a list of non-negative integers, result is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: The result list contains the elements of the array list, where each element is selected by the index calculated as (k - 1) % len(array) for each k in queries, and n, operations, and array remain unchanged.
    return result
    #The program returns the result list containing elements of the array list, where each element is selected by the index calculated as (k - 1) % len(array) for each k in queries, and n, operations, and array remain unchanged.

#Overall this is what the function does:Functionality: This function takes in a non-negative integer `n`, a list of operations where each operation is a tuple containing an integer type (1 or 2) and a non-negative integer value, and a list of non-negative integer queries. It processes the operations to construct a list of non-negative integers, and then uses this list to compute the result for each query by selecting an element from the list based on the query value. The function returns a list of results, one for each query, without modifying the original input variables `n`, operations, and queries.

#State of the program right berfore the function call: n is a positive integer, operations is a list of lists of two integers, queries is a list of positive integers, and the length of operations is n.
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the result of the function func_1 for the corresponding input values of n, operations, and queries. The length of the output list is equal to the number of iterations t. The values of n, operations, and queries are updated in each iteration, but their initial values are not affected by the loop.

#Overall this is what the function does:The function accepts three parameters: a positive integer n, a list of lists of two integers (operations), and a list of positive integers (queries). It processes the operations and queries based on the value of n, and returns a list of integers as a result. The function does not modify the input parameters. The purpose of the function is to perform a series of operations and queries based on the input values, and produce a list of results. The final state of the program after the function concludes is a list of integers, where each integer is the result of the function's processing for the corresponding input values.

