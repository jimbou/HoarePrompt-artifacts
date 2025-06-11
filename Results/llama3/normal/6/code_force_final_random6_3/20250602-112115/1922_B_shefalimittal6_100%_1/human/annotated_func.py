#State of the program right berfore the function call: stdin contains t+2t lines, where t is a positive integer. The first line contains one positive integer t. Each of the following t blocks of two lines contains a positive integer n and a list of n non-negative integers, respectively.
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        v = [0] * (n + 1)
        
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            v[x] += 1
        
        cnt = 0
        
        ans = 0
        
        for i in range(n + 1):
            if v[i] >= 2:
                ans += cnt * v[i] * (v[i] - 1) // 2
            if v[i] >= 3:
                ans += v[i] * (v[i] - 1) * (v[i] - 2) // 6
            cnt += v[i]
        
        results.append(str(ans))
        
    #State: `t` is 0, `data` is a list of strings split from the input, `idx` is `t*n+2*t`, `results` is a list containing `t` strings where each string is the sum of all combinations of pairs and triples of elements in `v`, `n` is greater than or equal to 0, `v` is a list of integers where the value at index `x` is `n` and all other indices are 0, `i` is `n`, `cnt` is the sum of all elements in `v`, `ans` is the sum of all combinations of pairs and triples of elements in `v`, `_` is `n-1`, `x` is an integer equal to the value at index `idx-1` of `data`.
    print('\n'.join(results))
    #This is printed: (empty string)

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain a positive integer t, followed by t blocks of two lines each. Each block contains a positive integer n and a list of n non-negative integers. The function calculates the sum of all combinations of pairs and triples of elements in each block and stores the results in a list. Finally, it prints the results, one per line.

