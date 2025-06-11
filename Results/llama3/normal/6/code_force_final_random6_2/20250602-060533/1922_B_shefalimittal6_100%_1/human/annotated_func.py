#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains an integer t (1 <= t <= 10^4). Each of the next t blocks of two lines contains an integer n (1 <= n <= 3*10^5) and n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= n). The sum of n over all blocks does not exceed 3*10^5.
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
        
    #State: idx is t+2t+2t+1, t is 0, results is a list containing t string elements where each element is the string representation of ans, data is a list of t+2t lines, n is an integer equal to the integer value at index idx-n-1 in data and is at least 0, v is a list of n+1 elements where the element at index x is n and all other elements are 0, _ is n-1, i is n+1, cnt is 2n, x is an integer equal to the value of the element at index idx-1 in data, and ans is either cnt * v[i] * (v[i] - 1) + v[i] * (v[i] - 1) * (v[i] - 2) // 6 if v[i] is greater than or equal to 3, or cnt * v[i] * (v[i] - 1) otherwise.
    print('\n'.join(results))
    #This is printed: the string representation of ans, repeated t times, where ans is either cnt * v[i] * (v[i] - 1) + v[i] * (v[i] - 1) * (v[i] - 2) // 6 if v[i] is greater than or equal to 3, or cnt * v[i] * (v[i] - 1) otherwise, and v[i] is n, and n is at least 0

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain an integer t, followed by t blocks of two lines, where the first line of each block contains an integer n, and the second line contains n space-separated integers. The function calculates a value for each block based on the occurrences of each integer and prints the results as a list of strings, one for each block. The calculation involves counting the number of pairs and triples of each integer and summing up the counts. The function does not modify the input data and does not have any side effects other than printing the results.

