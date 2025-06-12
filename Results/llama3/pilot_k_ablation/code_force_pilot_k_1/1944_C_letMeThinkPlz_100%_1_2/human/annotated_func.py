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
        
    #State: t is an integer and is 0, n is not defined, arr is not defined, counter is not defined, ans is not defined, once is not defined, stdin contains no input.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a list of integers. It then processes each test case to find the smallest positive integer that is not present in the list or is present only once. The function prints the result for each test case and consumes all input from standard input, leaving it empty.

