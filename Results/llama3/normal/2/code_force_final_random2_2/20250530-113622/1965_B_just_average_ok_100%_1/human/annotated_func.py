#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(21)]
        
        idx = -1
        
        for i in range(len(nums)):
            if nums[i] > k:
                idx = i - 1
                break
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: n is an integer between 2 and 10^6 inclusive, k is an integer between 1 and n inclusive, nums is a list of 21 integers where each integer is a power of 2 except for three integers which are k - nums[idx], k + 1, and k + nums[idx] + 1, i is between 0 and 20 inclusive, idx is between -1 and 20 inclusive, stdin is empty, the length of the list nums which is 21 is being printed, and the list of 21 integers in nums is being printed

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 1000) representing the number of test cases. For each test case, it reads two integers n and k (2 <= n <= 10^6, 1 <= k <= n) from stdin. It then generates a list of 21 integers, where each integer is a power of 2, except for three integers which are k - nums[idx], k + 1, and k + nums[idx] + 1. The function prints the length of the list (21) and the list of 21 integers. The function repeats this process for each test case.

