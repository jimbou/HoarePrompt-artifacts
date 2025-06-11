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
        
    #State: n is an integer between 2 and 50 (inclusive), m is an integer between 2 and 50 (inclusive) and equal to the value of the first input, arr is a list of n integers between 0 and 99 (inclusive), ans is either True or False depending on whether the list of integers formed by the digits of arr[i - 1] and arr[i] is sorted in ascending order or not for all i from m - 1 to 1, i is 0, stdin contains t-n test cases, each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 99), and 'YES' if all elements in the list arr are in non-decreasing order, or 'NO' otherwise is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then checks if the list of integers can be transformed into a non-decreasing order by rearranging the digits of adjacent elements. If the list can be transformed, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for all test cases provided in the input.

