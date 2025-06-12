#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three space-separated integers a, b, and c (0 <= a, b, c <= 10^9) representing the number of introverts, extroverts, and universals, respectively.
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: stdin is empty, p, q, and r are the values of the last test case, and the output contains t lines, each containing either (p - q // 3, -1) if r is greater than or equal to q % 3, or (-1, -1) if r is less than q % 3 for each test case.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains three integers representing the number of introverts, extroverts, and universals. It then processes each test case by calculating the number of extroverts and universals combined, and prints the result of subtracting one-third of this combined number from the number of introverts if the number of universals is greater than or equal to the remainder of the combined number divided by three, otherwise it prints -1. The function continues this process until all test cases have been processed, leaving stdin empty and the output containing the results of each test case.

