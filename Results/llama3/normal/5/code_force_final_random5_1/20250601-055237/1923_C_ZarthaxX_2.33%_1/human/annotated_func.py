#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a list of two integers, and then a list of integers. The list of integers is followed by multiple queries, each query being a list of two integers.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: n is an integer, i is n+1, q is an integer, nums is a list of n integers, ones is a list of n+1 integers where ones[i] is the number of 1s in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums minus i, stdin contains multiple test cases with a list of integers and multiple queries, each query being a list of two integers.
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
        
    #State: n is an integer, i is n+1, q is 0, nums is a list of n integers, ones is a list of n+1 integers, sum is a list of n+1 integers, stdin is empty.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains an integer, a list of two integers, and a list of integers, followed by multiple queries. For each query, it determines whether a certain condition is met based on the number of 1s and the sum of the elements in a specified range of the list of integers. It prints 'YES' if the condition is met and 'NO' otherwise, until all queries for all test cases have been processed, leaving the standard input empty.

