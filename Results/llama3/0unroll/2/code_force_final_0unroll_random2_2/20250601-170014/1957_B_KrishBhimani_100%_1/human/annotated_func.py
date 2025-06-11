#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers n and k (1 ≤ n ≤ 2 * 10^5, 1 ≤ k ≤ 10^9).
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
        
    #State: The output state will contain t lines, each representing the result of the corresponding input. For each input, if n is 1, the output will be k. If n is greater than 1, the output will be a list of n numbers, where the first number is the largest power of 2 less than k, the second number is k minus the first number, and the remaining numbers are 0.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts multiple lines of input, where the first line contains an integer t, representing the number of test cases. Each subsequent line contains two integers, n and k. For each test case, if n is 1, it prints k. If n is greater than 1, it calculates the largest power of 2 less than k, subtracts this value from k, and prints the result as a list of n numbers, where the first number is the largest power of 2 less than k, the second number is k minus the first number, and the remaining numbers are 0. The function prints t lines of output, each corresponding to the result of the corresponding input.

