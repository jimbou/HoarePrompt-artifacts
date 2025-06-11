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
        
    #State: The output state will contain 'YES' or 'NO' for each test case, indicating whether the array can be sorted in ascending order by repeatedly replacing the first element with the smallest digit of the previous element. The value of 'n' will be the same as in the initial state, and the input will be consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer array. It then checks if the array can be sorted in ascending order by repeatedly replacing the first element with the smallest digit of the previous element. For each test case, it prints 'YES' if the array can be sorted and 'NO' otherwise. The function consumes the input and does not modify the original array.

