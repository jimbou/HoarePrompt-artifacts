#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines: the first line contains one integer n (1 <= n <= 3 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= n).
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
        
    #State: Output State: The variable 'results' contains 't' number of integers, each representing the sum of the indices of the first occurrence of each duplicate element in the sorted array 'a' for each test case, 'current_index' is equal to 2 * t + 1, and all other variables remain unchanged.
    for result in results:
        print(result)
        
    #State: Output State: The variable 'results' contains 't' number of integers, each representing the sum of the indices of the first occurrence of each duplicate element in the sorted array 'a' for each test case, 'current_index' is equal to 2 * t + 1, and all other variables remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then sorts the integers and calculates the sum of the indices of the first occurrence of each duplicate element in the sorted array. The function returns the sum of these indices for each test case, printing the results to standard output.

