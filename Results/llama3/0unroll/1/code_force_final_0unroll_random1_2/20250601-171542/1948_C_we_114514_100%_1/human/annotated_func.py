#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: The loop completes all iterations without returning 'No', indicating that the conditions within the loop are not met for any iteration. The state of the variables remains unchanged, with n still being a positive even integer, row1 and row2 being strings of length n consisting of '<' and '>' characters, and half_n being an integer equal to half of n.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns 'No'
    #State: *The loop completes all iterations without returning 'No', indicating that the conditions within the loop are not met for any iteration. The state of the variables remains unchanged, with n still being a positive even integer, row1 and row2 being strings of length n consisting of '<' and '>' characters, and half_n being an integer equal to half of n. Additionally, it is not the case that the last character of row1 is '<' and the second last character of row2 is '<'.
    return 'Yes'
    #The program returns 'Yes', indicating that the conditions within the loop were not met for any iteration, and the state of the variables remains unchanged, with n still being a positive even integer, row1 and row2 being strings of length n consisting of '<' and '>' characters, and half_n being an integer equal to half of n.

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) based on the given conditions of two rows of '<' and '>' characters, returning 'Yes' if the movement is possible and 'No' otherwise.

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
        
    #State: Output State: t is a positive integer equal to 0, n is an even positive integer, row1 and row2 are strings of length n consisting of '<' and '>' characters, results is a list of t items, each item is the output of func_1(n, row1, row2), stdin contains 0 inputs.
    print('\n'.join(results))
    #This is printed: (empty string)

#Overall this is what the function does:Reads input for a specified number of test cases, processes each case by calling a function with the input values, and prints the results.

