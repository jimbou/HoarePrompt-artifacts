#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains an integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times.
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The number of duplicate integers in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a sequence of n integers. It then counts the number of duplicate integers in each test case and prints the count. The function processes all test cases in the input and outputs the duplicate count for each case.

