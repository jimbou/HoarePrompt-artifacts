#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers n and k (1 <= n <= 2*10^5, 1 <= k <= 10^9).
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: The output state will contain t lines, each containing n integers. If n is 1, the line will contain the value of k. If n is greater than 1, the line will contain a list of n integers, where the first integer is the largest power of 2 less than k, the second integer is the difference between k and the first integer, and the remaining integers are all 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, if n is 1, it prints the value of k. If n is greater than 1, it calculates the largest power of 2 less than k, subtracts this value from k, and prints the result as a list of n integers, where the first integer is the largest power of 2 less than k, the second integer is the difference between k and the first integer, and the remaining integers are all 0. The function repeats this process for each test case, printing the results in the specified format.

