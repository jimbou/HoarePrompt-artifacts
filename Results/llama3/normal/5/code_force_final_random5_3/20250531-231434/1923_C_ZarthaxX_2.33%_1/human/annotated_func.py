#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two space-separated integers, then a space-separated list of integers, and then multiple lines of two space-separated integers. The first integer is the number of test cases. The first integer of the second line of each test case is the length of the list of integers. The second integer of the second line of each test case is the number of queries. The list of integers contains positive integers. The first integer of each query is the start index of the subarray (1-indexed). The second integer of each query is the end index of the subarray (1-indexed). The number of queries does not exceed the length of the list of integers.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: n is an integer greater than or equal to 0, i is equal to n, q is an integer, nums is a list of positive integers, ones is a list of integers where ones[i] is equal to ones[i - 1] plus 1 if nums[i - 1] is 1, otherwise ones[i] is equal to ones[i - 1], sum is a list of integers where sum[i] is equal to sum[i - 1] plus nums[i - 1] minus 1, stdin contains multiple test cases with reduced input.
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
        
    #State: n is an integer greater than or equal to 0, i is equal to n, q is an integer greater than or equal to 0, nums is a list of positive integers, ones is a list of integers where ones[i] is equal to ones[i - 1] plus 1 if nums[i - 1] is 1, otherwise ones[i] is equal to ones[i - 1], sum is a list of integers where sum[i] is equal to sum[i - 1] plus nums[i - 1] minus 1, onesInRange is an integer equal to ones[r] minus ones[l - 1], sumInRange is an integer equal to sum[r] minus sum[l - 1], l is an integer equal to the first integer from the input, r is an integer equal to the second integer from the input. If 2 * onesInRange + (r - l + 1) - onesInRange is less than or equal to sumInRange, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a list of positive integers and a series of queries. For each query, it determines whether a subarray within the list can be transformed into a sequence of consecutive integers by replacing some elements with 1. The function prints 'YES' if such a transformation is possible and 'NO' otherwise.

