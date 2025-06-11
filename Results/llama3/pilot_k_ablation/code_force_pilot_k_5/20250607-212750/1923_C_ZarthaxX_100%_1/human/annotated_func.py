#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains an integer n and q, followed by a list of n integers, and then q queries, each consisting of two integers l and r.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: n is an integer greater than or equal to 0, q is an integer, nums is a list of n integers, ones is a list of n+1 integers where ones[i] is equal to the number of 1's in nums from index 0 to i-1, sum is a list of n+1 integers where sum[i] is equal to the sum of nums from index 0 to i-1, i is equal to n, stdin contains t-1 test cases.
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
        
    #State: n is an integer greater than or equal to 0, q is an integer equal to 0, nums is a list of n integers, ones is a list of n+1 integers where ones[i] is equal to the number of 1's in nums from index 0 to i-1, sum is a list of n+1 integers where sum[i] is equal to the sum of nums from index 0 to i-1, i is equal to n, stdin contains t-q test cases, _ is q.

#Overall this is what the function does:This function processes a series of test cases from standard input. Each test case consists of an integer n and q, followed by a list of n integers, and then q queries, each consisting of two integers l and r. The function calculates the number of 1's and the sum of the integers in the list up to each index, and then uses this information to answer each query. For each query, it checks if the sum of the integers in the range [l, r] is greater than or equal to twice the number of 1's in the range plus the length of the range minus the number of 1's in the range. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function processes all queries for each test case and then moves on to the next test case.

