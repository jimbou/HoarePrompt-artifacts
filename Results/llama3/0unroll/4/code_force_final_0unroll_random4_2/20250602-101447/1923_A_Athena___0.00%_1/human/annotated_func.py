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
        
    #State: The output state will contain t lines, each representing the result of a test case. Each line will first contain the list of integers from the test case with all leading and trailing zeros removed, followed by the number of zeros in the remaining list. The value of t remains unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a list of integers. It removes leading and trailing zeros from each list, counts the remaining zeros, and prints the modified list followed by the count of zeros. The function processes multiple test cases and outputs the results for each case, leaving the original input unchanged.

