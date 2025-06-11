#State of the program right berfore the function call: n is a non-negative integer, operations is a list of tuples where each tuple contains two integers, the first integer is either 1 or 2, and the second integer is a non-negative integer, queries is a list of non-negative integers.
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
        
    #State: n is a non-negative integer, operations is an empty list, queries is a list of non-negative integers, array is a list of non-negative integers, result is an empty list.
    for k in queries:
        result.append(array[(k - 1) % len(array)])
        
    #State: n is a non-negative integer, operations is an empty list, queries is an empty list, array is a list of non-negative integers, result is a list containing the element at index (k - 1) % len(array) of array for each query k in the initial queries list.
    return result
    #The program returns a list of non-negative integers, where each integer is the element at index (k - 1) % len(array) of array for each query k in the initial empty queries list, which means the list is empty.

#Overall this is what the function does:The function takes a non-negative integer n, a list of operations, and a list of queries as input. It performs a series of operations on an array, where each operation is either appending a value to the array or duplicating the array. After all operations are performed, the function uses the queries to extract elements from the array at specific indices, wrapping around to the start of the array if necessary. The function returns a list of the extracted elements.

#State of the program right berfore the function call: n is a positive integer, operations is a list of n lists, each containing two integers, and queries is a list of integers.
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        
        operations = [list(map(int, input().split())) for _ in range(n)]
        
        queries = list(map(int, input().split()))
        
        result = func_1(n, operations, queries)
        
        print(*result)
        
    #State: n is an integer equal to the first input integer, q is an integer equal to the second input integer, operations is a list of n lists, each containing two integers from stdin, queries is a list of integers from stdin, result is the output of func_1(n, operations, queries), t is equal to the initial value of t, stdin is empty, and the result of func_1(n, operations, queries) is printed t times.

#Overall this is what the function does:This function takes as input a positive integer n, a list of n lists of two integers (operations), and a list of integers (queries). It processes the operations and queries, and returns a result. The function is called t times, where t is an input integer, and the result is printed t times. The function does not modify the input variables n, operations, queries, or t. The purpose of the function is to perform some operation on the input data and return a result, which is then printed. The final state of the program is that the result of the function is printed t times, and the input variables remain unchanged.

