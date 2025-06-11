#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50) and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 99).
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
        
    #State: The loop will have executed n times, where n is the initial value of the variable n. The variable m will have been reassigned to the value of the input integer in each iteration, and the variable arr will have been reassigned to a list of integers parsed from the input string in each iteration. The variable ans will have been set to True or False depending on whether the list arr is sorted in descending order after the inner loop executes. The output of the loop will be a string 'YES' if ans is True, and 'NO' if ans is False, printed to the console n times. The initial value of n will remain unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It checks if the integers can be sorted in descending order by repeatedly replacing the smaller of two adjacent elements with the largest digit of the larger element. If the integers can be sorted, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for the specified number of test cases.

