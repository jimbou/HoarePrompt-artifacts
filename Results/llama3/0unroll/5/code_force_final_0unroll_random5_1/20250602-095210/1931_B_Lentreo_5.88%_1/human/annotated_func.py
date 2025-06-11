#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5), followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9). The sum of a_i is divisible by n.
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
        
    #State: The output state will contain 't' number of lines, each containing either 'YES' or 'NO'. 'YES' will be printed if the sum of differences between each non-zero number and the last number in the list is zero, otherwise 'NO' will be printed. The value of 't' and the input test cases remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case. It calculates the sum of differences between each non-zero number and the last number in the list, and prints 'YES' if the sum is zero, otherwise 'NO'. The function does not modify the input values and only outputs the result for each test case.

