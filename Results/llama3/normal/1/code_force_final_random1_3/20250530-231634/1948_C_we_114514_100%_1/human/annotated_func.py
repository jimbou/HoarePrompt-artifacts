#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: `n` is a positive even integer, `row1` and `row2` are strings of length `n` consisting of '<' and '>' characters, `half_n` is an integer equal to half of the value of `n`, `i` is `half_n - 1`. If `row1[2 * i + 1]` is '<' and either `row2[2 * i]` or `row2[2 * i + 2]` is '<', the program returns 'No'. Otherwise, the program does not return any value.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: *`n` is a positive even integer, `row1` and `row2` are strings of length `n` consisting of '<' and '>' characters, `half_n` is an integer equal to half of the value of `n`, `i` is `half_n - 1`. If `row1[2 * i + 1]` is '<' and either `row2[2 * i]` or `row2[2 * i + 2]` is '<', the program returns 'No'. Otherwise, the program does not return any value. Additionally, either `row1[n - 1]` is not '<' or `row2[n - 2]` is not '<'.
    return 'Yes'
    #The program returns 'Yes'.

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) based on the given row configurations. The function takes three parameters: a positive even integer `n` and two strings `row1` and `row2` of length `n` consisting of '<' and '>' characters. It returns 'Yes' if the robot can reach the destination and 'No' otherwise, considering the robot's movement restrictions imposed by the row configurations.

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
        
    #State: t is an integer greater than 0, results is a list containing t elements which are the return values of func_1(n, row1, row2), n is an even positive integer, row1 is a string of length n consisting of '<' and '>' characters, row2 is a string of length n consisting of '<' and '>' characters, _ is t-1, stdin contains 0 inputs.
    print('\n'.join(results))
    #This is printed: a sequence of t values, each representing the result of calling func_1 with the given arguments (where t is an integer greater than 0)

#Overall this is what the function does:This function reads input, processes each test case, and prints the results. It takes no arguments but reads from standard input. For each test case, it reads an even positive integer n and two strings row1 and row2 of length n consisting of '<' and '>' characters. It then calls another function func_1 with these inputs and appends the result to a list. After processing all test cases, it prints the results as a sequence of values, each representing the result of calling func_1 with the given arguments.

