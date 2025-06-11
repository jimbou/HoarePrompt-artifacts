#State of the program right berfore the function call: **stdin contains multiple test cases. Each test case consists of three parts:
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: n is an integer, q is an integer, nums is a list of n integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, stdin contains multiple test cases minus one.
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
        
    #State: n is an integer, q is a non-negative integer, nums is a list of n integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, stdin contains multiple test cases minus q.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads an integer n and q, followed by a list of n integers. It then calculates the cumulative count of 1's and the cumulative sum of the integers in the list. After that, it reads q queries, each consisting of two integers l and r. For each query, it checks if the sum of the integers in the range [l, r] is greater than or equal to twice the count of 1's in the range plus the length of the range minus the count of 1's. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function continues this process until all test cases have been processed.

