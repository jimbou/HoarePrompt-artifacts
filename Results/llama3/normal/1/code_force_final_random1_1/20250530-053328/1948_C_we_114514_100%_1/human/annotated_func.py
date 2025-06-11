#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n, consisting only of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The loop executes until `i` is equal to `half_n - 1`, at which point it terminates. If at any point during the loop's execution `row1[2 * i + 1]` is '<' and either `row2[2 * i]` or `row2[2 * i + 2]` is '<', the program returns 'No'. Otherwise, the program continues execution without returning a value.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'.
    #State: *The loop executes until `i` is equal to `half_n - 1`, at which point it terminates. If at any point during the loop's execution `row1[2 * i + 1]` is '<' and either `row2[2 * i]` or `row2[2 * i + 2]` is '<', the program returns 'No'. Otherwise, the program continues execution without returning a value. Additionally, it is not the case that `row1[n - 1]` is '<' and `row2[n - 2]` is '<'.
    return 'Yes'
    #The program returns 'Yes'

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) given two rows of length n, consisting of '<' and '>' characters, and returns 'Yes' if the movement is possible and 'No' otherwise.

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
        
    #State: t is at least t, results is a list containing t elements, each element is the output of func_1(n, row1, row2), n is an even positive integer, row1 is a string of length n consisting of '<' and '>' characters, row2 is a string of length n consisting of '<' and '>' characters, stdin contains 0 inputs.
    print('\n'.join(results))
    #This is printed: the results of the function func_1(n, row1, row2) for t number of times (where n is an even positive integer, row1 and row2 are strings of length n consisting of '<' and '>' characters, and t is at least t)

#Overall this is what the function does:This function reads input from the user, processes each test case, and prints the results. It accepts no parameters and returns nothing. The function reads a positive integer t, then for each test case, it reads an even positive integer n and two strings of length n consisting of '<' and '>' characters. It calls the function func_1 with these inputs and appends the result to a list. After processing all test cases, it prints the results of func_1 for each test case. The final state of the program is that the input has been processed and the results have been printed to the console.

