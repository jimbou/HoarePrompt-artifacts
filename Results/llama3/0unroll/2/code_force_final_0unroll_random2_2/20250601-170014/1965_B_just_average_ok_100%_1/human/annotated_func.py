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
        
    #State: The output state will contain the number of elements in the list "nums" and the elements in the list "nums" for each iteration of the loop. The number of elements in "nums" will be 5 for each iteration, and the elements will be the powers of 2 from 2^0 to 2^20, excluding the power of 2 that is greater than k, and including k - 2^idx, k + 1, and k + 2^idx + 1, where idx is the index of the power of 2 that is greater than k.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of numbers containing powers of 2 from 2^0 to 2^20, excluding the power of 2 greater than k, and including three additional numbers: k minus the largest power of 2 less than or equal to k, k plus 1, and k plus the largest power of 2 less than or equal to k plus 1. The function then prints the length of this list and its elements.

