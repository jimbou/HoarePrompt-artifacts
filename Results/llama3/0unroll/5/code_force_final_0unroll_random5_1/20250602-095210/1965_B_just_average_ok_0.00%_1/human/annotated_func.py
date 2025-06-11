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
        
    #State: The output state will contain the length of the list "nums" and the elements of the list "nums" for each test case. The list "nums" will contain 24 elements, which are powers of 2 from 2^0 to 2^23, and three additional elements: k - 2^idx, k + 1, and k + 2^idx + 1, where idx is the largest index such that 2^idx is less than or equal to k. The element 2^idx will be removed from the list.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it generates a list of 24 elements containing powers of 2 from 2^0 to 2^23, then modifies the list by removing the largest power of 2 less than or equal to k, and appending three new elements: k minus the removed power of 2, k plus 1, and k plus the removed power of 2 plus 1. The function then prints the length of the modified list and its elements for each test case.

