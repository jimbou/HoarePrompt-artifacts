#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then for each test case, two integers (n and k) separated by a space. n and k are positive integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: n is an integer greater than or equal to 1, k is an integer greater than or equal to 1, nums is a list of 24 integers where each integer is a power of 2 except for the last three elements which are k - nums[4], k + 1, and k + nums[4] + 1, idx is 4, stdin is empty, the length of the list nums which is 24 is being printed, and the elements of the list nums which are 21 powers of 2 and the last three elements which are k - nums[4], k + 1, and k + nums[4] + 1 are being printed

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts two inputs: the number of test cases and, for each test case, two integers (n and k) separated by a space. The function generates a list of 24 integers, where the first 21 elements are powers of 2, and the last three elements are k - 2^4, k + 1, and k + 2^4 + 1. It then prints the length of the list (24) and the elements of the list. The function repeats this process for each test case.

