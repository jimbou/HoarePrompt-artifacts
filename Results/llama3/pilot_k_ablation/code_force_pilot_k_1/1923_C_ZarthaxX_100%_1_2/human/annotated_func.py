#State of the program right berfore the function call: stdin contains a series of inputs: first an integer, then a series of pairs of integers, then a list of integers, and finally a series of pairs of integers. The first integer is a positive integer. Each pair of integers is a pair of positive integers where the first integer is less than or equal to the second integer. The list of integers is a list of positive integers.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: n is a positive integer, q is a positive integer, nums is a list of positive integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, stdin contains a series of pairs of integers, i is n.
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
        
    #State: n is a positive integer, q is 0, nums is a list of positive integers, ones is a list of n+1 integers where ones[i] is the count of 1's in the first i elements of nums, sum is a list of n+1 integers where sum[i] is the sum of the first i elements of nums, i is n, _ is q, stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes a series of queries, and prints 'YES' or 'NO' for each query based on a condition involving the count of 1's and the sum of elements in a subarray. The function takes no arguments and returns no value, but it modifies the state of the program by consuming input from stdin and printing output to the console. The function's purpose is to determine whether a given condition is met for each query, and it performs this action by iterating over the queries, calculating the count of 1's and the sum of elements in the specified subarray, and printing the result.

