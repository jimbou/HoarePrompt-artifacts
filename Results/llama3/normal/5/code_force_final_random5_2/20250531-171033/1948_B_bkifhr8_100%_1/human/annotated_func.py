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
        
    #State: n is an integer between 1 and 10^3 inclusive and is equal to 0, _ is n-1, m is 0, i is -m, arr is a list of integers. If any pair of adjacent elements in arr were not sorted in ascending order, then ans is False and 'NO' is printed. Otherwise, ans is True and 'YES' is printed, and either 'NO' or 'YES' is printed indicating whether the array `arr` is sorted in ascending order or not.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It checks if the integers in each test case can be sorted in ascending order by only replacing the first element of each pair of adjacent elements that are not in ascending order with the smallest digit of the first element. If all pairs of adjacent elements can be sorted in this way, it prints 'YES', otherwise it prints 'NO'. The function processes all test cases and prints the result for each one.

