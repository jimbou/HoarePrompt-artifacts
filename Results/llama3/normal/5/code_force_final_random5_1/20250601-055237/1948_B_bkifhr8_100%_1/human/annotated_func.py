#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 99).
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
        
    #State: n is 1, m is an integer greater than 1, arr is a list of m integers between 0 and 99 where all elements are sorted in ascending order, ans is True, and 'YES' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the integers can be sorted in ascending order by repeatedly replacing the largest two consecutive elements with their digits sorted in ascending order. If the integers can be sorted, it prints 'YES', otherwise it prints 'NO'. The function processes multiple test cases and prints the result for each case.

