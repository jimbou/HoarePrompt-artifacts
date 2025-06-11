#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of integers, and then multiple lines each containing two integers. The first integer is the number of test cases. The first integer of each test case is the length of the list and the second integer is the number of queries. The list contains integers greater than 0. The queries contain two integers each, representing the borders of a subarray, and are 1-indexed. The sum of the lengths of the lists over all test cases does not exceed 3 * 10^5, and the sum of the number of queries over all test cases does not exceed 3 * 10^5.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: The variable ones is a list of integers where each element at index i represents the count of 1's in the first i elements of the list nums. The variable sum is a list of integers where each element at index i represents the sum of the first i elements of the list nums minus i.
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
        
    #State: Output State: The variable ones is a list of integers where each element at index i represents the count of 1's in the first i elements of the list nums. The variable sum is a list of integers where each element at index i represents the sum of the first i elements of the list nums minus i.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers and a series of queries. It calculates the cumulative count of 1's and the cumulative sum of the list minus the index for each prefix of the list. Then, for each query, it determines whether a subarray within the given borders can be transformed into a list of consecutive integers starting from 1 by replacing some elements with 1, and prints 'YES' if possible and 'NO' otherwise.

