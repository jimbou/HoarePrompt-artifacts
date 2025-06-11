#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 2 * 10^4) and then a list of integers (0 <= integer < 2 * 10^5). The sum of the lengths of the lists over all test cases does not exceed 2 * 10^5.
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
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: Output State: The output state after the loop executes all the iterations is that the variable 'ans' will hold the smallest positive integer that is not present in the input list 'arr' or the smallest positive integer that appears only once in the list, and this value will be printed to the console for each test case. The variable 't' will remain unchanged, and the variable 'stdin' will be empty after all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a list of integers. For each test case, it finds the smallest positive integer that is either not present in the list or appears only once, and prints this value to the console. The function processes all test cases and empties the standard input.

