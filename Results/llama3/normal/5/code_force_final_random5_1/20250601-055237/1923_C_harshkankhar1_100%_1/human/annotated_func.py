#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two integers n and q, followed by n integers c_1, c_2, ..., c_n, followed by q pairs of integers l_i and r_i. All integers are positive, 1 <= t <= 10^4, 1 <= n, q <= 3 * 10^5, 1 <= c_i <= 10^9, 1 <= l_i <= r_i <= n.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: t is reduced by 1, stdin contains t-1 test cases, i is n, q is a positive integer, a is a list of n+1 integers where the first element is 0 and the remaining elements are the n integers c_1, c_2, ..., c_n, b is a list of n+1 integers where the first element is 0, and the remaining elements are the cumulative sums of 1 if a[j] > 1 else 2 for j in range(1, n+1)
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: t is reduced by 1, i is n, q is 0, a is a list of n+1 integers where the first element is 0 and the remaining elements are the cumulative sums of a[j] for j in range(1, n+1), b is a list of n+1 integers where the first element is 0, and the remaining elements are the cumulative sums of 1 if a[j] > 1 else 2 for j in range(1, n+1), x is an integer, y is an integer, stdin contains t-q test cases.

#Overall this is what the function does:This function reads input from stdin, processes test cases, and prints 'YES' or 'NO' for each query. It takes no parameters and returns no values. The function's purpose is to determine whether a given range of integers in a list has a cumulative sum less than the cumulative sum of a calculated value (1 if the integer is greater than 1, otherwise 2) for the same range. The function processes all test cases and queries, printing the results for each query.

