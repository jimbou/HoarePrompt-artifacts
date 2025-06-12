#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an integer between 0 and 10^4, `current_index` is `1 + sum of all n`, `results` is a list containing the sum of hashing[a[i]] for all i where a[i] is equal to a[i + 1] for each iteration, `data` is a list of strings representing the input data, `input` is a function that reads from sys.stdin, `n` is an integer equal to the value of the string at the previous current_index in the data list for the last iteration, `a` is a sorted list containing the integer values of the strings at the current_index in the data list for the last iteration, `i` is the last value of n-1, `ans` is the sum of hashing[a[i]] for all i where a[i] is equal to a[i + 1] for the last iteration, hashing is a dictionary containing the key-value pair {a[i]: sum of indices of a[i] in the list a} for all i for the last iteration. If t is 0, then current_index is 1, results is an empty list, and the other variables remain unchanged.
    for result in results:
        print(result)
        
    #State: `t` is an integer between 0 and 10^4, `current_index` is `1 + sum of all n`, `results` is a list containing the sum of hashing[a[i]] for all i where a[i] is equal to a[i + 1] for each iteration, `data` is a list of strings representing the input data, `input` is a function that reads from sys.stdin, `n` is an integer equal to the value of the string at the previous current_index in the data list for the last iteration, `a` is a sorted list containing the integer values of the strings at the current_index in the data list for the last iteration, `i` is the last value of n-1, `ans` is the sum of hashing[a[i]] for all i where a[i] is equal to a[i + 1] for the last iteration, hashing is a dictionary containing the key-value pair {a[i]: sum of indices of a[i] in the list a} for all i for the last iteration, all elements in the results list have been printed. If t is 0, then current_index is 1, results is an empty list, and the other variables remain unchanged. If results is an empty list, then no elements have been printed.

#Overall this is what the function does:Reads input from standard input, processes it, and prints the results. The input consists of an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The function sorts each test case, calculates the sum of the indices of equal adjacent elements, and stores these sums in a list. Finally, it prints each sum in the list. If there are no test cases (t = 0), the function does not print anything.

