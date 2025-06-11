#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n). Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The number of duplicate integers in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. It then counts the number of duplicate integers in each test case and prints the result. The function assumes that each integer from 1 to n appears in the sequence at most twice and that the sum of n over all test cases does not exceed 2 * 10^5.

