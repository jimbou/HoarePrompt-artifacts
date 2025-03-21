#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
def func():
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
        
    #State: For each of the `t` test cases, the output will be the length of the modified `nums` list followed by the elements of the modified `nums` list. The modifications for each test case are independent and do not affect the others.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it constructs a list of numbers based on powers of 2 up to \(2^{20}\), modifies this list by adding and removing specific elements related to `k`, and then outputs the length of the modified list followed by its elements. The results for each test case are independent of one another.

