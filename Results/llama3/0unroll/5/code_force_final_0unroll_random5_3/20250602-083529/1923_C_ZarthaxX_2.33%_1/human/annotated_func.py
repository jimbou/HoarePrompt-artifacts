#State of the program right berfore the function call: stdin contains multiple inputs: the first line contains one integer, each of the following lines contains two integers, and then a list of integers, and then multiple lines each containing two integers. The first integer is a positive integer, the second integer in each of the following lines is a positive integer and less or equal than the first integer in the same line. The list of integers contains positive integers.
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
        
    #State: Output State: The ones list and the sum list remain unchanged, as they are not modified within the loop. The loop iterates q times, processing input ranges and printing 'YES' or 'NO' based on the conditions within the loop.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints 'YES' or 'NO' for each query. It first reads an integer n and q, then a list of n integers, and then q pairs of integers. It calculates the cumulative count of 1's and the cumulative sum of the list minus the index. For each query, it checks if a certain condition is met based on the calculated values and prints 'YES' if the condition is met, otherwise prints 'NO'. The function does not modify the input list or the calculated cumulative values.

