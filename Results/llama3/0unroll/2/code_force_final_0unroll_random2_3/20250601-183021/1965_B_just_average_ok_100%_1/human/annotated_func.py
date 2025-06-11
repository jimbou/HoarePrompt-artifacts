#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of test cases. Each test case consists of two space-separated integers n and k such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: The output state is a series of test cases, each consisting of two space-separated integers n and k, such that 2 <= n <= 10^6 and 1 <= k <= n. The output state is identical to the initial state, as the loop does not modify the input values.

#Overall this is what the function does:This function generates and prints a series of test cases, each consisting of a list of integers. The function takes no parameters and does not modify the input values. It reads the number of test cases and the test cases themselves from standard input, processes the test cases, and prints the results to standard output. The function does not return any values.

