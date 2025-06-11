#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^9).
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        arr = []
        
        k0 = k
        
        i = 0
        
        while k:
            if k & 1 == 1:
                arr.append(i)
            k = k >> 1
            i += 1
        
        ans = []
        
        c = 0
        
        for i in arr:
            if c == n - 1:
                ans.append(k0 - sum(ans))
                break
            c += 1
            ans.append(1 << i)
        
        ans += [0] * (n - len(ans))
        
        print(*ans)
        
    #State: `n` is an integer between 1 and 2 * 10^5, `k` is 0, `_` is equal to `t`, stdin is empty, `l1` is a list containing two strings, `arr` is an empty list, `k0` is an integer between 1 and 10^9, `i` is equal to the number of times the loop executed, `c` is equal to `n` + the number of times the loop executed minus 1, `ans` is a list containing `n` elements: `k0`, 1, 1 << `i`, and `n` - `i` - 2 zeros if `c` is equal to `n` - 1, otherwise `ans` is a list containing `n` elements: `k0`, 1, 1 << `i`, and `n` - `i` - 2 zeros, and the elements of `ans` are printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of n elements, where the first elements are powers of 2 corresponding to the binary representation of k, and the remaining elements are zeros, except for the last element, which is the remaining value of k after subtracting the sum of the powers of 2. The function then prints the generated list for each test case.

