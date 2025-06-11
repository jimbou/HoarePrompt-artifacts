#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). For each test case, the first line contains a single integer n (1 <= n <= 2 * 10^5) and the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times.
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: stdin contains multiple test cases, open(0) is a file object that must have at least 2*t + 1 lines, line is the (2*t + 1)th line, and the difference between the number of tokens in the (2*t + 1)th line and the number of unique tokens in the (2*t + 1)th line is being printed

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the difference between the total number of integers and the number of unique integers in each test case. It assumes that the input is well-formed, with the first line containing the number of test cases, and each test case consisting of two lines: the first line containing a single integer (n), and the second line containing n integers. The function does not perform any error checking or handling.

