#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5), then n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
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
        
    #State: The output state after the loop executes all the iterations will be a series of 'YES' or 'NO' printed to the console, depending on whether the sum of the differences between each number and the last number in the list is zero or not, for each test case. The value of `t` will be unchanged, and the input from stdin will be consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the sum of the differences between each number and the last number in the list is zero. If the sum is zero, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for each test case and consumes all input from standard input.

