#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1). At least one a_i is 1.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: The output state will be a list of integers representing the number of zeros in each test case, after removing leading and trailing zeros from the input list. The input list will be modified to remove leading and trailing zeros. The variable 't' will remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the number of zeros in each test case after removing leading and trailing zeros. It modifies the input list by removing leading and trailing zeros, but leaves the initial number of test cases unchanged.

