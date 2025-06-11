#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 100), and the second line contains n space-separated integers a_i (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The output state will contain t lines, each representing the sum of the maximum of all but the last number and the last number in each test case. The value of t remains unchanged, and the input state of stdin is consumed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a list of integers. For each test case, it calculates the sum of the maximum of all but the last number and the last number, and prints this sum as output. The function consumes the input state of stdin and produces t lines of output, where t is the number of test cases.

