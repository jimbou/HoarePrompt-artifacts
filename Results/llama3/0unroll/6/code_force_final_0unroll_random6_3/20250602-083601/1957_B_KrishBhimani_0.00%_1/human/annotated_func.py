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
        
    #State: The output state will be a series of lines, each containing a list of integers. The number of lines will be equal to the value of t in the initial state. Each list will contain n integers, where n is the first integer in the corresponding line of the initial state. The integers in each list will be the binary representation of the number k (the second integer in the corresponding line of the initial state), with the least significant bit first, followed by zeros to fill the list to length n. If the length of the binary representation of k is less than n, the list will be padded with zeros on the left.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of integers representing the binary representation of k, with the least significant bit first, and pads the list with zeros to a length of n. The function then prints each list on a separate line.

