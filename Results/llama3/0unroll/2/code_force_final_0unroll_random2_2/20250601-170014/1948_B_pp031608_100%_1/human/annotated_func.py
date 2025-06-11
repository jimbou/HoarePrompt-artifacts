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
        
    #State: The loop has executed n times, and for each test case, it has printed 'YES' if the array can be sorted in ascending order by repeatedly replacing the first element with the smallest digit of the previous element, and 'NO' otherwise. The value of n has been decremented to 1, and the stdin contains no more test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer array. It then checks if the array can be sorted in ascending order by repeatedly replacing the first element with the smallest digit of the previous element. For each test case, it prints 'YES' if the array can be sorted in this way and 'NO' otherwise.

