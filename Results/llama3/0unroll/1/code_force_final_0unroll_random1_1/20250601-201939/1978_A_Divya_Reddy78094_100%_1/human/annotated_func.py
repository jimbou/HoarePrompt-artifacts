#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The output state will be the sum of the maximum of all numbers excluding the last number and the last number itself, for each test case. The output will be printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the sum of the maximum of all numbers excluding the last number and the last number itself for each test case. It accepts no parameters and returns no value, instead printing the results directly to the console. The function's purpose is to calculate and display the specified sum for each test case in the input.

