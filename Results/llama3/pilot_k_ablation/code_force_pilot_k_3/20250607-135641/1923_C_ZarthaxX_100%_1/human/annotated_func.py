#State of the program right berfore the function call: stdin contains an integer t, then t times: two integers n and q, a list of n integers, and q pairs of integers. All integers are greater than 0.
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: i is n, ones is a list of n+1 integers where ones[i] is ones[i - 1] plus 1 if nums[i - 1] is 1, otherwise ones[i] is ones[i - 1], sum is a list of n+1 integers where sum[i] is sum[i - 1] plus nums[i - 1].
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
        
    #State: i is n, ones is a list of n+1 integers where ones[i] is ones[i - 1] plus 1 if nums[i - 1] is 1, otherwise ones[i] is ones[i - 1], sum is a list of n+1 integers where sum[i] is sum[i - 1] plus nums[i - 1], q is 0, stdin contains a space-separated list of integers minus q inputs.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints 'YES' or 'NO' for each query. It takes no arguments and returns no value. The input is expected to contain an integer t, followed by t sets of data. Each set of data contains two integers n and q, a list of n integers, and q pairs of integers. The function calculates the cumulative sum and count of ones in the list of integers, then answers q queries by checking if a certain condition is met for each query. The condition is based on the sum and count of ones in a specified range. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function processes all queries and does not modify the input data.

