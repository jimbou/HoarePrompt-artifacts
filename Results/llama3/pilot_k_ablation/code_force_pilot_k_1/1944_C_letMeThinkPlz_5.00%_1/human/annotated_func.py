#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a positive integer (1 <= n <= 2 * 10^5). The second input is a list of n integers (0 <= a_i < n). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0, _ is t, n is undefined, arr is undefined, counter is an empty dictionary, stdin is empty, ans is undefined, once is False, and all the answers are printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n integers. It then finds the smallest positive integer that is not present in the list or the smallest positive integer that appears only once in the list, and prints this value for each test case. The function processes all test cases and prints all answers before terminating.

