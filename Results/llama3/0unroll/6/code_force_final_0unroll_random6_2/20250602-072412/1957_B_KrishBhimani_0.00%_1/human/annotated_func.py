#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers n and k (1 <= n <= 2 * 10^5, 1 <= k <= 10^9).
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
        
    #State: The output state will contain t lines, each containing n space-separated integers. The integers in each line represent the binary representation of the number k, with the least significant bit on the left and the most significant bit on the right. If n is greater than the number of bits in k, the remaining bits will be filled with zeros.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts a series of lines as input, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains two integers n and k. The function then generates a binary representation of k, with the least significant bit on the left and the most significant bit on the right, and fills the remaining bits with zeros if n is greater than the number of bits in k. Finally, it prints the resulting binary representation as a series of space-separated integers, with each line representing a test case.

