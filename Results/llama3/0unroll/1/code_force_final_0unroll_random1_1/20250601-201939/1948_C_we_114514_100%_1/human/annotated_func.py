#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: Output State: The loop finishes all its iterations without returning 'No', and the values of row1, row2, n, and half_n remain unchanged.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: The loop finishes all its iterations without returning 'No', and the values of row1, row2, n, and half_n remain unchanged. Additionally, either row1[n - 1] is not '<' or row2[n - 2] is not '<'.
    return 'Yes'
    #The program returns 'Yes'

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) given two rows of '<' and '>' characters, returning 'Yes' if possible and 'No' otherwise.

#State of the program right berfore the function call: t is a positive integer, n is an even positive integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    读取输入并处理每个测试用例。
    """
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        row1 = input()
        
        row2 = input()
        
        results.append(func_1(n, row1, row2))
        
    #State: results is a list of t elements, each element is the output of func_1 for the corresponding input, t is an integer, stdin is empty.
    print('\n'.join(results))
    #This is printed: the results of func_1 for each input, one per line

#Overall this is what the function does:Reads input for a specified number of test cases, processes each case by calling func_1 with the provided input values, and stores the results in a list. The function then prints the results of func_1 for each test case, one per line.

