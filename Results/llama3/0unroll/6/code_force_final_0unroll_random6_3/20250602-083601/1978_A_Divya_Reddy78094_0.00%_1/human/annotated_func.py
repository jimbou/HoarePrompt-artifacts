#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: The sum of the two largest integers in each test case, printed on a new line for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains a list of integers. It then identifies the two largest integers in each test case, calculates their sum, and prints the result for each test case. The function does not return any values, instead, it outputs the results directly to the console.

