#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
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
        
    #State: The loop has finished executing, and the final output state is determined by the last iteration of the loop. The value of the loop counter `_` is equal to `t`, the number of test cases. The variables `n` and `k` have the values of the last test case. The list `nums` contains 21 integers, where each integer is a power of 2 except for three integers: `k - nums[idx]`, `k + 1`, and `k + nums[idx] + 1`. The index `idx` is the index of the largest power of 2 in `nums` that is less than or equal to `k`. The variable `i` has the value 20. The standard input `stdin` is empty, as all test cases have been processed. The length of the list `nums` is 21, and the list `nums` is printed with its 21 integers.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it generates a list of 21 integers, initially containing powers of 2 from 2^0 to 2^20. It then finds the largest power of 2 less than or equal to k, replaces it with three new integers (k - largest_power, k + 1, and k + largest_power + 1), and prints the length and the modified list of integers. The function processes all test cases and prints the results for each case.

