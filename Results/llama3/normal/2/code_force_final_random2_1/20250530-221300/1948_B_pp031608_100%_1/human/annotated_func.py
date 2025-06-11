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
        
    #State: n is an integer between 2 and 50, m is an integer and is at least 2, arr is a list of m integers where each integer is between 0 and 99, stdin contains 0 test cases, i is 0, ans is a boolean value. If arr[i] is less than arr[i - 1] at any point during the loop execution, then arr[i - 1] is the first digit of its original value, nums is a list of integers where the first elements are the digits of arr[i - 1] and the last element is arr[i]. If nums is not sorted in ascending order at any point during the loop execution, then ans is False. Otherwise, ans remains True, and either 'NO' or 'YES' is printed depending on whether ans is False or True respectively.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the integers can be transformed into a sorted list by repeatedly replacing the first digit of an integer with the smallest digit of the original integer, if the integer is smaller than the previous one. The function prints 'YES' if the transformation is possible and 'NO' otherwise.

