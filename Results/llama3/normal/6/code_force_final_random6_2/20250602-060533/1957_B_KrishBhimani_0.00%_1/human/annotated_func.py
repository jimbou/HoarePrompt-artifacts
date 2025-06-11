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
        
    #State: `n` is an integer between 1 and 2 * 10^5, `k` is 0, `i` is the last element in the list `arr`, `arr` is an empty list, stdin is empty, `c` is equal to `n`, `ans` is a list containing all the elements which are 2^i for all `i` in `arr`, and `k0 - sum(ans)` is updated to `k0 - sum(ans + [0] * (n - len(ans)))`, and the elements of `ans` which are all the elements which are 2^i for all `i` in `arr` are being printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads two integers n and k, where n is the number of elements in the output list and k is a binary number. The function then generates a list of integers, where each integer is a power of 2 corresponding to the positions of the set bits in the binary representation of k. If the length of this list is less than n, it pads the list with zeros to make its length equal to n. Finally, it prints the elements of the list.

