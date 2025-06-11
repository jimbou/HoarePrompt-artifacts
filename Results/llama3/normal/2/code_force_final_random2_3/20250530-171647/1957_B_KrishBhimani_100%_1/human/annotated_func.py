#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers n and k (1 ≤ n ≤ 2⋅10^5, 1 ≤ k ≤ 10^9).
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
        
    #State: n is an integer between 1 and 2⋅10^5, k is an integer between 1 and 10^9, stdin is empty, arr is an empty list, k0 is an integer between 1 and 10^9 equal to k, ans is a list of length n containing the values (1 << i) - 1, k - sum(ans), and n - len(ans) zeros if n is larger than 1 and k is larger than 2^i, otherwise n - len(ans) - 1 zeros, i is the largest integer such that 2^i is less than or equal to k, and temp is 2^i. If n is 1, k is printed. Otherwise, the largest power of 2 less than k minus 1, the remaining value after subtracting the sum of the first element and the zeros from k, and a list of zeros with a length of n minus the length of ans are printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It reads multiple lines of input, where the first line contains a single integer t, and each of the following t lines contains two integers n and k. For each pair of n and k, if n is 1, it prints k. Otherwise, it calculates the largest power of 2 less than k, subtracts 1 from it, and prints this value along with the remaining value after subtracting the sum of this value and n-2 zeros from k, and a list of zeros with a length of n-2. The function continues this process until it has processed all input lines, at which point stdin is empty.

