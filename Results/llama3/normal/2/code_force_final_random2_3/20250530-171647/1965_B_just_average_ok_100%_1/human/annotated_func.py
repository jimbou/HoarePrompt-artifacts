#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t pairs of integers n and k (2 <= n <= 10^6, 1 <= k <= n).
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
        
    #State: n is an integer greater than or equal to 1, k is an integer, nums is a list of 23 integers containing powers of 2 from 2^0 to 2^20 except 2^20, nums contains k - 2^20 + 1, k + 1, and k + 2^20 + 1, idx is 20, _ is the value of t, i is 21, and the length of the list nums which is 23 is being printed, and this is printed: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, k - 2^20 + 1, k + 1, and k + 2^20 + 1

#Overall this is what the function does:This function generates and prints a list of 23 integers containing powers of 2 from 2^0 to 2^20 except 2^20, and three additional numbers: k - 2^20 + 1, k + 1, and k + 2^20 + 1, where k is an integer input. The function takes two inputs: an integer t (1 <= t <= 1000) and t pairs of integers n and k (2 <= n <= 10^6, 1 <= k <= n). It iterates over each pair of inputs, generates the list of numbers, and prints the length of the list and the list itself.

