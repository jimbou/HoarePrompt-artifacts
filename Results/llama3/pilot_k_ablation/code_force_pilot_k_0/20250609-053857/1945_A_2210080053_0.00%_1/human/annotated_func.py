#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers a, b, c (0 <= a, b, c <= 10^9) — the number of introverts, extroverts, and universals, respectively.
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: The output will be the number of introverts and extroverts after considering the universals as extroverts, or -1 if the number of universals is less than the remainder of the total extroverts divided by 3, for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains three integers representing the number of introverts, extroverts, and universals. It considers universals as extroverts, calculates the new number of introverts and extroverts, and prints the result. If the number of universals is less than the remainder of the total extroverts divided by 3, it prints -1 instead. The function iterates through all test cases and provides the corresponding output for each case.

