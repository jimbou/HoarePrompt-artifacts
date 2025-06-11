#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: Output State: The loop finishes all its iterations without returning 'No'.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns the string 'No'
    #State: The loop finishes all its iterations without returning 'No'. Either `row1[n - 1]` is not '<' or `row2[n - 2]` is not '<' (or both).
    return 'Yes'
    #The program returns 'Yes' because the loop finished all its iterations without returning 'No', indicating that either `row1[n - 1]` is not '<' or `row2[n - 2]` is not '<' (or both).

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) given two rows of length n consisting of '<' and '>' characters, returning 'Yes' if the move is possible and 'No' otherwise.

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
        
    #State: t is an integer, results is a list of t elements, each of which is the result of func_1(n, row1, row2) for the corresponding input, stdin is empty.
    print('\n'.join(results))
    #This is printed: the results of calling func_1 for each of the t input values, separated by newline characters

#Overall this is what the function does:Reads input, processes each test case by calling func_1 with the provided input values, and prints the results separated by newline characters.

