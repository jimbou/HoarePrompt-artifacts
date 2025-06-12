#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The first integer is a non-negative integer. The list of integers is a list of non-negative integers. The length of the list is equal to the first integer. The integers in the list are in the range 0 to the first integer.
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
        
    #State: `stdin` is empty, `data` is a list of strings, `current_index` is `t` times the value of `data[1]` plus 1, `t` is 0, `results` is a list containing the sum of the indices of all consecutive equal elements in `a` for each iteration of the loop, `hashing` is an empty dictionary, `n` is an integer equal to the value of `data[1]`, `ans` is the sum of the indices of all consecutive equal elements in `a` for the last iteration of the loop, `a` is a sorted list containing the integer values of `data[2]` to `data[n+1]` for the last iteration of the loop. If `t` is 0, the loop does not execute and `hashing` is an empty dictionary, `ans` is 0, `results` is an empty list, `current_index` is 1.
    for result in results:
        print(result)
        
    #State: `stdin` is empty, `data` is a list of strings, `current_index` is `t` times the value of `data[1]` plus 1, `t` is 0, `results` is a list containing the sum of the indices of all consecutive equal elements in `a` for each iteration of the loop, `hashing` is an empty dictionary, `n` is an integer equal to the value of `data[1]`, `ans` is the sum of the indices of all consecutive equal elements in `a` for the last iteration of the loop, `a` is a sorted list containing the integer values of `data[2]` to `data[n+1]` for the last iteration of the loop, and all elements in `results` have been printed. If `t` is 0, the loop does not execute and `hashing` is an empty dictionary, `ans` is 0, `results` is an empty list, `current_index` is 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a non-negative integer and a list of non-negative integers. It then calculates the sum of the indices of all consecutive equal elements in the list for each test case and prints the results. If there are no test cases, it does not perform any calculations and does not print anything.

