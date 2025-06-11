#State of the program right berfore the function call: stdin contains t+2*t*n integers: first an integer t (1 <= t <= 10^4), then t times: first an integer n (1 <= n <= 3*10^5) and then n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3*10^5.
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
        
    #State: t is 0, results is a list containing the sum of the products of the indices of consecutive equal elements in a for all test cases, current_index is the length of data, data is a list of strings representing the input integers, _ is t, n is the integer value of the string at index current_index-1 in data, a is an empty list, i is -1, ans is 0, and hashing is an empty dictionary.
    for result in results:
        print(result)
        
    #State: The loop has finished executing, and all elements in the `results` list have been printed. The values of `t`, `current_index`, `data`, `_`, `n`, `a`, `i`, `ans`, and `hashing` remain unchanged.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain an integer t, followed by t sets of data, each set consisting of an integer n and n integers a_1 to a_n. The function calculates the sum of the products of the indices of consecutive equal elements in each set and stores these sums in a list. Finally, it prints each sum in the list. The function does not modify the input data or any external state, and its only output is the printed results.

