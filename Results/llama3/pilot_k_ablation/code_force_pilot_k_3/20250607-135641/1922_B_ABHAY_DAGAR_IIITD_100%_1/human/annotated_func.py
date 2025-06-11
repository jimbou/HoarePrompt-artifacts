#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains one integer n, and the second line contains n integers a_1, a_2, ..., a_n. 1 <= t <= 10^4, 1 <= n <= 3 * 10^5, and 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
    input = sys.stdin.read
    data = input().split()
    current_index = 0
    t = int(data[current_index])
    current_index += 1
    results = []
    for _ in range(t):
        hashing = {}
        
        n = int(data[current_index])
        
        current_index += 1
        
        a = []
        
        for i in range(n):
            a.append(int(data[current_index]))
            current_index += 1
        
        a.sort()
        
        ans = 0
        
        for i in range(n - 1):
            if a[i] not in hashing:
                hashing[a[i]] = 0
            hashing[a[i]] += i
            if a[i] == a[i + 1]:
                ans += hashing[a[i]]
        
        results.append(ans)
        
    #State: `t` is 0, `current_index` is `n+n+...+n+t`, `results` is a list containing the sum of the values of `hashing` dictionary for all the keys that have at least two consecutive occurrences in `a` t times, `data` is a list of strings split from the input, `n` is an integer equal to the value of `data` at index `n+n+...+n+t-1` and must be at least `n-1`, `a` is a sorted list containing the integer values of `data` at indices `n+n+...+n+t` to `n+n+...+n+t+n-1`, `i` is `n-1`, `_` is `t-1`, `hashing` is a dictionary that contains the keys `a[0]` to `a[n-2]` with values `0` to `n-2`, and `ans` is the sum of the values of `hashing` dictionary for all the keys that have at least two consecutive occurrences in `a`.
    for result in results:
        print(result)
        
    #State: `t` is the length of `results` minus 1, `current_index` is `n+n+...+n+t`, `results` is a list containing the sum of the values of `hashing` dictionary for all the keys that have at least two consecutive occurrences in `a` t times, `data` is a list of strings split from the input, `n` is an integer equal to the value of `data` at index `n+n+...+n+t-1` and must be at least `n-1`, `a` is a sorted list containing the integer values of `data` at indices `n+n+...+n+t` to `n+n+...+n+t+n-1`, `i` is `n-1`, `_` is `t-1`, `hashing` is a dictionary that contains the keys `a[0]` to `a[n-2]` with values `0` to `n-2`, `ans` is the sum of the values of `hashing` dictionary for all the keys that have at least two consecutive occurrences in `a`, and the last element in the list `results` which is the sum of the values of `hashing` dictionary for all the keys that have at least two consecutive occurrences in `a` is being printed.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain multiple test cases, each consisting of two lines: the first line contains the number of integers in the test case, and the second line contains the integers themselves. The function sorts the integers in each test case, counts the number of consecutive occurrences of each integer, and calculates the sum of the indices of these occurrences. It then prints the sum for each test case. The function does not modify the input data and does not have any side effects other than printing the results.

