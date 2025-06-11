#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains a single integer n, and the second line contains n integers a_1, a_2, ..., a_n. 1 <= t <= 10^3, 2 <= n <= 50, and 0 <= a_i <= 99.
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
        
    #State: The loop has executed t-1 times, and for each test case, it has printed 'YES' if the array can be sorted in non-decreasing order by reversing a subarray, and 'NO' otherwise. The value of n is still between 2 and 50, and stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints whether each test case's array can be sorted in non-decreasing order by reversing a subarray. It iterates through each test case, checks if the array can be sorted by reversing a subarray, and prints 'YES' if possible and 'NO' otherwise. The function does not modify the input array or store any results; it only prints the outcome for each test case.

