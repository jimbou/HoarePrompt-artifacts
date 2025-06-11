#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: `stdin` contains a multiple of 2 plus 1 lines, `line` is the last line, and the difference between the number of tokens in the last line and the number of unique tokens in the last line is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. It then calculates and prints the difference between the total number of integers and the number of unique integers in the second line of each test case.

