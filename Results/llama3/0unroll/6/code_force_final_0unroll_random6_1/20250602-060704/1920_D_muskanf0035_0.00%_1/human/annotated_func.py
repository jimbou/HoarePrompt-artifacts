#State of the program right berfore the function call: n is a non-negative integer, operations is a list of tuples where each tuple contains two integers, the first integer is either 1 or 2, and the second integer is a non-negative integer, queries is a list of non-negative integers.
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
        
    #State: Output State: The result list contains the elements of the array list, where each element is selected based on the index calculated by (k - 1) % len(array) for each k in queries. The other variables remain unchanged.
    return result
    #The program returns the result list that contains elements of the array list, where each element is selected based on the index calculated by (k - 1) % len(array) for each k in queries. The other variables remain unchanged.

#Overall this is what the function does:This function takes in three parameters: a non-negative integer n, a list of operations where each operation is a tuple containing an operation type (1 or 2) and a non-negative integer value, and a list of non-negative integer queries. It processes the operations to construct an array, where operation type 1 appends the value to the array and operation type 2 duplicates the current array. Then, for each query, it calculates an index based on the query value and the length of the array, and appends the element at that index to the result list. The function returns the result list, leaving the input variables unchanged.

#State of the program right berfore the function call: n is a positive integer, operations is a list of n lists, each containing two integers, queries is a list of positive integers.
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: Output State: The final state after the loop executes all the iterations is that the variable `result` will hold the output of the function `func_1` for the last iteration of the loop, and the variables `n`, `operations`, and `queries` will hold the values from the last iteration of the loop. The variable `t` will remain unchanged as it is not modified within the loop.

#Overall this is what the function does:The function `func_1` takes three parameters: a positive integer `n`, a list of `n` lists of two integers `operations`, and a list of positive integers `queries`. It performs a series of operations based on the input and returns a result. The function's purpose is to process the input data and generate an output, which is then printed. The final state of the program after the function concludes is that the variable `result` holds the output of the function for the last iteration of the loop, and the variables `n`, `operations`, and `queries` hold the values from the last iteration of the loop.

