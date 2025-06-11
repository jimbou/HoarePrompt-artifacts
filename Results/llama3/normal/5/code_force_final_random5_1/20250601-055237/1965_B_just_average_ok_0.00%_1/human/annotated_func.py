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
        
    #State: nums is a list of 24 elements, each a power of 2 from 2^1 to 2^23, and three additional elements: k - 2^23, k + 1, and k + 2^23 + 1, idx is 23, n is an integer, k is an integer, stdin is empty, and the length of the list nums which is 27 is being printed, and the list nums is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it generates a list of 24 elements representing powers of 2 from 2^1 to 2^23, and then appends three additional elements: k - 2^23, k + 1, and k + 2^23 + 1. The function then prints the length of the resulting list (which is always 27) and the list itself. The function does not modify the input values n and k, and it does not use the value of n in any way. The function assumes that the input is well-formed and does not include any error checking.

