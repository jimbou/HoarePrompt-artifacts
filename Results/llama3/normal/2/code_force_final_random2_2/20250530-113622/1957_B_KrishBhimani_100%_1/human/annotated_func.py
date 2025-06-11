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
        
    #State: The loop has executed for the number of times specified by the first integer in the first line of stdin. The values of n and k have been updated to the values in the last line of stdin. If n is 1, the value of k is printed. If n is larger than 1, an empty list arr is created, k0 is set to k, temp is a power of 2 that is less than k, i is the number of times the loop executed, ans is a list containing (1 << i) - 1, k - sum(ans), and n - len(ans) zeros, and the elements of the list ans are printed: (1 << i) - 1, k - sum(ans), and n - len(ans) zeros.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a single integer t, and each of the following t lines contains two integers n and k. For each pair of n and k, if n is 1, it prints the value of k. If n is larger than 1, it calculates a list of values based on k and prints the list, which contains a power of 2 less than k, the difference between k and the sum of the list, and n-2 zeros. The function repeats this process for the number of times specified by the first integer t.

