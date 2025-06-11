#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of integers, and then multiple lines each containing two integers. The first integer is the number of test cases. The second integer is the number of queries. The list of integers is a list of positive integers. The two integers are the left and right borders of the subarray (1-indexed). The number of queries is equal to the second integer. The length of the list of integers is equal to the first integer.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: The ones list contains the cumulative count of 1's in the nums list, and the sum list contains the cumulative sum of the nums list minus the index.
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
        
    #State: Output State: The ones list contains the cumulative count of 1's in the nums list, and the sum list contains the cumulative sum of the nums list minus the index.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer, a list of integers, and multiple queries. It then processes each test case by calculating the cumulative count of 1's and the cumulative sum of the list minus the index. For each query, it determines whether a subarray within the given borders can be transformed into a sequence of consecutive integers starting from 1 by replacing some elements with 1. If such a transformation is possible, it prints 'YES', otherwise it prints 'NO'.

