#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers (a_1, a_2, ..., a_n). The sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().strip().split()))
        
        last = nums[-1]
        
        curr = 0
        
        for i in nums:
            if i != 0:
                curr += i - last
        
        if curr == 0:
            print('YES')
        else:
            print('NO')
        
    #State: t is an integer representing the number of test cases and must be equal to 0, _ is equal to t, n is an integer, nums is a list of integers, last is an integer equal to the last element of the list of integers, curr is the sum of all elements in nums except the last one, i is the last element of the list of integers. No more 'YES' or 'NO' is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then checks if the sum of all elements in the list except the last one is equal to zero. If the sum is zero, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for all test cases.

