#State of the program right berfore the function call: n is a non-negative integer, operations is a list of tuples where each tuple contains two integers, the first integer is either 1 or 2, and the second integer is a non-negative integer, and queries is a list of non-negative integers.
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: `n` is a non-negative integer, `operations` is an empty list of tuples, `queries` is a list of non-negative integers, `array` is a list containing non-negative integers, `result` is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: Output State: `n` is a non-negative integer, `operations` is an empty list of tuples, `queries` is an empty list of non-negative integers, `array` is a list containing non-negative integers, `result` is a list containing the value of `array` at index `(k - 1) % len(array)` for each query `k` in the original list of queries.
    #
    #In natural language, after the loop executes all its iterations, the output state will have an empty list of queries, and the result list will contain the values from the array that correspond to each query in the original list of queries. The other variables remain unchanged.
    return result
    #The program returns a list of non-negative integers, where each integer is the value of `array` at index `(k - 1) % len(array)` for each query `k` in the original list of queries. The list `queries` is empty, and the other variables `n`, `operations`, and `array` remain unchanged.

#Overall this is what the function does:This function takes in a non-negative integer `n`, a list of operations where each operation is a tuple containing an operation type (1 or 2) and a non-negative integer value, and a list of non-negative integer queries. It processes the operations to construct an array by either appending values or duplicating the existing array. Then, it uses the constructed array to answer the queries by returning the values at indices corresponding to each query modulo the length of the array. The function returns a list of non-negative integers, where each integer is the value of the array at the index corresponding to each query. The original lists of operations and queries are emptied, while the other variables remain unchanged.

#State of the program right berfore the function call: n is a positive integer, operations is a list of n lists, each containing two integers, and queries is a list of integers.
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: n is an integer equal to the first input, q is an integer equal to the second input, operations is a list of n lists, each containing two integers from stdin, queries is a list of integers from stdin, t is equal to 0, _ is equal to t, result is the return value of func_1(n, operations, queries), stdin is empty, and the result of func_1(n, operations, queries) is being printed, and the result of func_1(n, operations, queries) which is stored in the variable result is being printed, and the elements of the result are being printed.

#Overall this is what the function does:This function takes three parameters: a positive integer n, a list of n lists (operations) where each sublist contains two integers, and a list of integers (queries). It processes the operations and queries, and returns a list of results. The function's purpose is to perform a series of operations based on the input queries and return the outcome. The final state of the program is that the result of the function is printed, with each element of the result printed separately.

