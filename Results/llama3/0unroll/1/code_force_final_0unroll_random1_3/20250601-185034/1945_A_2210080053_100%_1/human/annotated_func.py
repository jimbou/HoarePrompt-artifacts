#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains three space-separated integers a, b, and c (0 <= a, b, c <= 10^9) representing the number of introverts, extroverts, and universals, respectively.
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The output state will contain t lines, each containing a single integer. If the number of universals (c) is less than the remainder of the sum of extroverts and universals (b + c) divided by 3, the output will be -1. Otherwise, the output will be the number of introverts (a) minus the integer division of the sum of extroverts and universals (b + c) by 3.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of three integers representing the number of introverts, extroverts, and universals. It calculates the total number of extroverts and universals, and then prints the number of introverts minus the integer division of the total extroverts and universals by 3, unless the number of universals is less than the remainder of the total extroverts and universals divided by 3, in which case it prints -1. The function outputs one integer per test case, resulting in a total of t lines of output, where t is the number of test cases specified in the first line of input.

