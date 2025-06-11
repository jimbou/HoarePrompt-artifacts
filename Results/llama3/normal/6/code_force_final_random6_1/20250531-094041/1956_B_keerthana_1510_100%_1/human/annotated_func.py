#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The loop will execute until it has processed all the lines in the input, printing the difference between the total number of tokens and the number of unique tokens for each line that is 2 positions ahead of a multiple of 4 (i.e., lines at positions 2, 6, 10, ...).

#Overall this is what the function does:This function reads input from standard input, processes every other line starting from the third line, and prints the difference between the total number of integers and the number of unique integers on each processed line.

