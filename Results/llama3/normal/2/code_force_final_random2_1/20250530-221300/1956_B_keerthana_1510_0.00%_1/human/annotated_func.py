#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n). Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times.
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: elements is an empty list, stdin contains no test cases, open(0) has no lines, and the sum of the integer division of the count of each unique item in the list elements by 3 is being printed

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two lines. It then processes the second line of each test case, which contains a list of integers, and prints the sum of the integer division of the count of each unique item in the list by 3. After processing all test cases, the function leaves the input stream empty and the list of elements empty.

