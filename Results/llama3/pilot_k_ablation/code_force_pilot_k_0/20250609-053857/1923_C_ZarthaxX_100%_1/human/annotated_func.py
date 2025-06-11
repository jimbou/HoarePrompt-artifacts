#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and q (1 <= n, q <= 3 * 10^5), followed by n integers c_1, c_2, ..., c_n (1 <= c_i <= 10^9), and then q lines, each containing two integers l_i and r_i (1 <= l_i <= r_i <= n).
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1]
        
    #State: Output State: The ones list now contains the cumulative count of 1's in the nums list, where ones[i] represents the number of 1's from the start of the list to the i-th index. The sum list now contains the cumulative sum of the nums list, where sum[i] represents the sum of all numbers from the start of the list to the i-th index.
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
        
    #State: Output State: The loop has executed q iterations, and for each iteration, it has printed either 'YES' or 'NO' based on the condition 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange. The values of ones and sum lists remain unchanged as they are not modified within the loop.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts no parameters and returns no values. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of two integers n and q, representing the size of an array and the number of queries, respectively. The function then reads n integers into an array and q pairs of integers representing query ranges. For each query range, the function calculates the cumulative count of 1's and the cumulative sum within the range and prints 'YES' if a certain condition is met, and 'NO' otherwise. The function repeats this process for all test cases.

