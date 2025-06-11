#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 99).
    n = int(input())
    for _ in range(n):
        m = int(input())
        
        arr = [int(i) for i in input().split()]
        
        ans = True
        
        for i in range(m - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                nums = [int(i) for i in str(arr[i - 1])] + [arr[i]]
                if nums != sorted(nums):
                    ans = False
                    break
                arr[i - 1] = nums[0]
        
        print(['NO', 'YES'][ans])
        
    #State: n is an integer between 2 and 50 inclusive, m is an integer that must be at least 1, arr is a list of n integers where arr[0] is equal to nums[0], i is 0, and ans is True if nums is sorted in ascending order and arr[i] is not less than arr[i - 1], otherwise False. If arr[i] is less than arr[i - 1], then arr[-1] is equal to nums[0], nums is a list containing the digits of arr[-1] as integers and arr[0], and ans is False if nums is not sorted in ascending order. Otherwise, ans is True if nums is sorted in ascending order and arr[0] is not less than arr[-1]., and either 'YES' or 'NO' is printed

#Overall this is what the function does:This function reads input from the standard input, processes it, and prints either 'YES' or 'NO' to the standard output. It accepts a series of test cases, each consisting of an integer n followed by n integers. The function checks if the integers in each test case can be rearranged in ascending order by only rearranging the digits of the first integer. If the integers can be rearranged in ascending order, it prints 'YES'; otherwise, it prints 'NO'.

