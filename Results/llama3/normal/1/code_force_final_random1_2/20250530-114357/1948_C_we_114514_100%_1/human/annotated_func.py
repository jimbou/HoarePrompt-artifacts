#State of the program right berfore the function call: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters.
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
        
    #State: n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters, half_n is an integer equal to n divided by 2 and must be at least 3, i is half_n - 1. If row1[2 * i + 1] is '<' and either row2[2 * i] or row2[2 * i + 2] is '<', the program returns the string 'No'. Otherwise, no changes are made.
    if (row1[n - 1] == '<' and row2[n - 2] == '<') :
        return 'No'
        #The program returns the string 'No', which indicates that the conditions for row1 and row2 are not met, specifically that row1[2 * i + 1] is '<' and either row2[2 * i] or row2[2 * i + 2] is '<', where i is half_n - 1, half_n is n divided by 2 and is at least 3, and n is a positive even integer.
    #State: *n is a positive even integer, row1 and row2 are strings of length n consisting of '<' and '>' characters, half_n is an integer equal to n divided by 2 and must be at least 3, i is half_n - 1. If row1[2 * i + 1] is '<' and either row2[2 * i] or row2[2 * i + 2] is '<', the program returns the string 'No'. Otherwise, no changes are made. Additionally, either row1[n - 1] is not '<' or row2[n - 2] is not '<'.
    return 'Yes'
    #The program returns the string 'Yes'

#Overall this is what the function does:Determines whether a robot can move from position (1,1) to (2,n) based on the given conditions of two rows of '<' and '>' characters. The function takes three parameters: a positive even integer n, and two strings row1 and row2 of length n consisting of '<' and '>' characters. It returns 'Yes' if the robot can move, and 'No' otherwise. The function checks for specific conditions in the rows, and if any of these conditions are met, it immediately returns 'No'. If none of the conditions are met after checking all positions, it returns 'Yes'.

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
        
    #State: t is a positive integer equal to 0, n is an integer, row1 is a string of length n consisting of '<' and '>' characters, row2 is a string of length n consisting of '<' and '>' characters, results is a list containing t elements which are the return values of func_1(n, row1, row2), stdin is empty, _ is t-1
    print('\n'.join(results))
    #This is printed: (empty string)

#Overall this is what the function does:Reads input, processes each test case by calling func_1 with the provided parameters, and stores the results in a list. The function then prints the results as a newline-separated string. The input is consumed, and the standard input is left empty.

