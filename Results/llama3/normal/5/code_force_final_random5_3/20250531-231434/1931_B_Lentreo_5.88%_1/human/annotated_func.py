#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0, _ is t, stdin contains 0 test cases, n is an integer between 1 and 2 * 10^5, nums is an empty list, last is the last integer in the original list, and curr is the sum of the differences between each integer in the list and the last integer in the list, excluding the last integer itself and any zeros. If curr is 0, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It calculates the sum of differences between each integer (excluding the last one and zeros) and the last integer in the list. If this sum is zero, it prints 'YES', indicating that the list meets a certain condition. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

