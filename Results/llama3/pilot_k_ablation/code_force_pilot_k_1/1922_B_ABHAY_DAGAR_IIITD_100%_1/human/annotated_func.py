#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains an integer t (1 <= t <= 10^4). Each of the following t blocks of 2 lines contains an integer n (1 <= n <= 3*10^5) and n integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all test cases does not exceed 3*10^5.
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
        
    #State: `stdin` is empty, `data` contains `t+2t` lines from the original `stdin`, `current_index` is `t*(n+1)+1`, `t` is an integer between 1 and 10^4, `results` is a list containing the sum of the indices of the first occurrence of each duplicate element in `a` for each iteration of the loop, `a` is an empty list, `ans` is 0, `n` is an integer equal to the value at index `t` in `data`, `i` is `n-1`, `hashing` is an empty dictionary. If `t` is 0, then `results` is an empty list and `current_index` is 1.
    for result in results:
        print(result)
        
    #State: `stdin` is empty, `data` contains `t+2t` lines from the original `stdin`, `current_index` is `t*(n+1)+1`, `t` is an integer between 1 and 10^4, `results` is an empty list, `a` is an empty list, `ans` is 0, `n` is an integer equal to the value at index `t` in `data`, `i` is `n-1`, `hashing` is an empty dictionary. All elements of the `results` list have been printed. If `t` is 0, then `results` is an empty list and `current_index` is 1.

#Overall this is what the function does:Reads input from stdin, processes it in blocks of 2 lines, calculates the sum of indices of the first occurrence of each duplicate element in the second line of each block, and prints these sums. The function accepts no parameters and returns no value, but instead prints the calculated sums to the console. The input is expected to be in a specific format, with the first line containing an integer t, followed by t blocks of 2 lines, where the first line of each block contains an integer n, and the second line contains n integers. The function processes this input, calculates the desired sums, and prints them to the console, leaving the input stream empty.

