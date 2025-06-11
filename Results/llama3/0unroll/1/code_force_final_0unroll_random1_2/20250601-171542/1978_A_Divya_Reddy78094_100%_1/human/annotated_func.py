#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case contains an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The output state will be the sum of the maximum of all integers in each test case except the last integer and the last integer itself, printed for each test case. The value of `t` will remain unchanged, and the stdin will be empty after the loop execution.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer count of numbers followed by those numbers. It then calculates and prints the sum of the maximum of all numbers in each test case except the last number and the last number itself. The function processes all test cases provided in the input and leaves the input stream empty after execution.

