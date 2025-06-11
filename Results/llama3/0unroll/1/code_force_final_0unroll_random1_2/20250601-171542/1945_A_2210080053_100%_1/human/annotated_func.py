#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three space-separated integers a, b, and c (0 <= a, b, c <= 10^9) representing the number of introverts, extroverts, and universals, respectively.
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The output will be a list of integers, each representing the number of introverts and extroverts in a group, or -1 if the number of universals is less than the remainder of the division of the total number of extroverts by 3. The list will have a length equal to the number of test cases.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains three integers representing the number of introverts, extroverts, and universals. It then calculates the total number of extroverts by adding the number of universals to the number of extroverts. If the remainder of the division of the total number of extroverts by 3 is greater than or equal to the number of universals, it prints the difference between the number of introverts and the integer division of the total number of extroverts by 3. Otherwise, it prints -1. The function repeats this process for each test case and outputs a list of integers, each representing the result of the calculation for the corresponding test case.

