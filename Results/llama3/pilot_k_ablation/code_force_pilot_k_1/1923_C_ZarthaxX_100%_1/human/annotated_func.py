#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: n is an integer greater than 0, q is an integer, nums is a list of integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, stdin is empty.
    for _ in range(q):
        l, r = map(int, input().split(' '))
        
        if l == r:
            print('NO')
            continue
        
        onesInRange = ones[r] - ones[l - 1]
        
        sumInRange = sum[r] - sum[l - 1]
        
        if 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange:
            print('YES')
        else:
            print('NO')
        
    #State: n is an integer greater than 0, q is an integer that is at least 0, nums is a list of integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to the console. It takes no parameters and returns no value. The function reads an integer n and q from stdin, followed by a list of n integers. It then calculates the cumulative sum and count of 1's in the list. The function reads q queries from stdin, each consisting of two integers l and r. For each query, it checks if a certain condition is met based on the cumulative sum and count of 1's in the range [l, r]. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function continues this process until all queries have been processed, leaving the stdin empty.

