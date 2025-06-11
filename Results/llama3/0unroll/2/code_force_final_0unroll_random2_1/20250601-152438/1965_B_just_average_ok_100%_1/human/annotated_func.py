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
        
    #State: The output state will be a series of lines, where each line contains the length of the list 'nums' followed by the elements of 'nums' after the operations have been performed. The number of lines will be equal to the value of 't' in the initial state. The 'nums' list will contain powers of 2 from 2^0 to 2^20, with the exception of 2^idx, where idx is the index of the largest power of 2 less than or equal to 'k'. Additionally, the list will contain 'k', 'k+1', and 'k+2^idx+1'.

#Overall this is what the function does:The function generates a series of lists of integers based on input parameters 'n' and 'k'. For each input pair, it creates a list of powers of 2 from 2^0 to 2^20, removes the largest power of 2 less than or equal to 'k', and appends 'k', 'k+1', and 'k+2^idx+1' to the list, where 'idx' is the index of the removed power of 2. The function then prints the length of the modified list followed by its elements. The number of output lines is equal to the initial input 't', which specifies the number of input pairs.

