#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three integers a, b, c (0 <= a, b, c <= 10^9) representing the number of introverts, extroverts, and universals, respectively.
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The output will be the number of introverts and extroverts after the universals have been distributed among them. If the number of universals is less than the remainder of the division of the total number of extroverts by 3, the output will be -1. Otherwise, the number of introverts will be increased by the integer division of the total number of extroverts by 3, and the number of extroverts will be the remainder of the division of the total number of extroverts by 3.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains three integers representing the number of introverts, extroverts, and universals. It then distributes the universals among the introverts and extroverts, increasing the number of introverts by the integer division of the total number of extroverts by 3 and setting the number of extroverts to the remainder of the division of the total number of extroverts by 3. If the number of universals is less than the remainder of the division, it outputs -1. The function prints the resulting number of introverts and extroverts for each test case.

