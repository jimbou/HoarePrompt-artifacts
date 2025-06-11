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
        
    #State: Output State: The output state after the loop executes all the iterations is: n is a non-negative integer, operations is an empty list, queries is a list of non-negative integers, array is a list of non-negative integers, result is a list of non-negative integers where each element is the value of array at the index (k - 1) % len(array) for each k in queries.
    return result
    #The program returns a list of non-negative integers where each element is the value of array at the index (k - 1) % len(array) for each k in queries.

#Overall this is what the function does:This function takes a non-negative integer n, a list of operations, and a list of queries as input. It processes the operations by either appending a value to an array or duplicating the array. Then, it uses the queries to extract values from the processed array, where each query corresponds to an index in the array. The function returns a list of non-negative integers, where each integer is the value at the index specified by the corresponding query, wrapping around to the start of the array if the index exceeds its length.

#State of the program right berfore the function call: n is a positive integer, operations is a list of n lists, each containing two integers, queries is a list of positive integers.
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: Output State: The output state after the loop executes all the iterations is that the `result` variable will hold the output of the `func_1` function for each iteration, and this output will be printed to the console. The values of `n`, `operations`, and `queries` will be updated for each iteration based on the input provided. The value of `t` will remain unchanged as it is not modified within the loop.

#Overall this is what the function does:The function `func_1` takes three parameters: a positive integer `n`, a list of `n` lists of two integers `operations`, and a list of positive integers `queries`. It performs a series of operations based on the input and returns a result. The purpose of the function is to process the input data and produce an output that is printed to the console. The final state of the program after the function concludes is that the output of the function is stored in the `result` variable and printed to the console, while the input variables `n`, `operations`, and `queries` are updated for each iteration of the loop.

