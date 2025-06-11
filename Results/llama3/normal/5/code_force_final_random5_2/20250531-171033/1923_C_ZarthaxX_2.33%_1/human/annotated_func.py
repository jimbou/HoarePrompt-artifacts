#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three inputs: first two integers n and q, then a list of n integers, and finally q pairs of integers. All integers are positive.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: n is a positive integer, q is a positive integer, nums is a list of n positive integers, ones is a list of n+1 integers where ones[i] is the number of 1s in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums minus i, stdin contains multiple test cases - 1, i is n.
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
        
    #State: n is a positive integer, q is a positive integer, nums is a list of n positive integers, ones is a list of n+1 integers where ones[i] is the number of 1s in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums minus i, i is n, stdin contains multiple test cases - q.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n, a positive integer q, a list of n positive integers, and q pairs of integers. It then processes each test case by iterating over the list of integers, counting the number of 1s and calculating the sum of the integers minus their indices. For each pair of integers in the test case, it checks if a certain condition is met based on the count of 1s and the sum, and prints 'YES' or 'NO' accordingly. The function repeats this process for all test cases in the input.

