#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: The sum of the two largest integers in each test case will be printed to the console, and the value of `t` will remain unchanged.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of integers. It then sorts each list in descending order and prints the sum of the two largest integers in each list. The function does not modify the input values or store any results, only printing the sums to the console.

