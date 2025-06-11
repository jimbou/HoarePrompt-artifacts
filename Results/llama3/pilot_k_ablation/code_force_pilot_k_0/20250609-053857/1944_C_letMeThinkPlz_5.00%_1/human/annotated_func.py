#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
                break
        
        print(ans)
        
    #State: The loop will have printed the smallest positive integer that is not present in the input list for each test case. The variable 't' remains unchanged, stdin is empty, and the variables 'n', 'arr', 'counter', 'ans', and 'once' are in their initial states.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds and prints the smallest positive integer that is not present in the input list for each test case.

