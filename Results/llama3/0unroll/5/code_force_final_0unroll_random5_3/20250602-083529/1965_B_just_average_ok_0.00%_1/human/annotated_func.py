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
        
    #State: The output state will contain t lines, each containing the length of the modified list of numbers followed by the modified list of numbers. The length will be 24, and the list will contain the numbers from 1 to 2^23, with the number 2^idx replaced by k - 2^idx, k + 1, and k + 2^idx + 1, where idx is the largest integer such that 2^idx is less than or equal to k.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then generates a list of numbers from 1 to 2^23, replaces the number 2^idx with three new numbers (k - 2^idx, k + 1, and k + 2^idx + 1), where idx is the largest integer such that 2^idx is less than or equal to k, and prints the length of the modified list followed by the modified list itself. The function repeats this process for each test case.

