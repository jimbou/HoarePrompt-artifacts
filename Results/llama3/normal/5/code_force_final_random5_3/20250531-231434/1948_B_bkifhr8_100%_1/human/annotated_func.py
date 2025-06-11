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
        
    #State: `n` is an integer between 2 and 50 (inclusive), `m` is an integer greater than 1, `arr` is a list of `m` integers between 0 and 99 (inclusive) where `arr[0]` is the first digit of `arr[m-1]`, either 'YES' or 'NO' has been printed, `i` is 1, `ans` is True or False, `nums` is undefined, `stdin` is empty, and either 'YES' or 'NO' is printed depending on the value of `ans`.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case. It takes an integer t (1 <= t <= 10^3) followed by t test cases, where each test case consists of an integer n (2 <= n <= 50) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 99). The function checks if the given list of integers can be rearranged in non-decreasing order by only swapping adjacent elements and replacing the first digit of the first element with the first digit of the last element. If the list can be rearranged, it prints 'YES', otherwise it prints 'NO'.

