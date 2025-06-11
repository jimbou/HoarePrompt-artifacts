#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(24)]
        
        idx = 0
        
        while k >= 1 << idx:
            idx += 1
        
        idx -= 1
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: n is an integer between 2 and 10^6 inclusive, k is an integer greater than or equal to 1, nums is a list of 24 integers where each integer is a power of 2 except for the last three elements which are k - nums[22], k + 1, and k + nums[22] + 1 respectively, idx is 23, stdin contains 0 lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n), and the length of the list nums which is 24 is being printed, and the list nums is being printed which contains 24 integers where each integer is a power of 2 except for the last three elements which are k - nums[22], k + 1, and k + nums[22] + 1 respectively

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then generates a list of 24 integers, where the first 22 elements are powers of 2, and the last three elements are k - 2^22, k + 1, and k + 2^22 + 1 respectively. The function prints the length of this list (which is always 24) and the list itself. The function repeats this process for each test case in the input.

