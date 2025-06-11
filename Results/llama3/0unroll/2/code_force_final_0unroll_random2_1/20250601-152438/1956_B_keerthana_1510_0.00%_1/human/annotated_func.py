#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times.
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: The output will be the sum of the counts of each unique integer in the input list divided by 3, for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains a list of integers. It then calculates and prints the sum of the counts of each unique integer in the list divided by 3, for each test case.

