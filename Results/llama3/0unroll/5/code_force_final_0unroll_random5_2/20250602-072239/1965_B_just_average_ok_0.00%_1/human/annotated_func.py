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
        
    #State: The output state will contain the length of the list 'nums' and the elements of the list 'nums' for each iteration of the loop. The length of 'nums' will be 4 for each iteration, and the elements will be the calculated values based on the input 'n' and 'k'. The output will be in the format: "4 a b c d" where a, b, c, and d are the calculated values.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of numbers based on the given k and calculates new values by performing bitwise operations and arithmetic additions. The function then prints the length of the resulting list and its elements. The output for each test case is a list of four numbers, which are the calculated values based on the input k. The function repeats this process for the specified number of test cases.

