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
        
    #State: k is 0, i is the last element in the list, arr is an empty list, n is an integer between 1 and 2 * 10^5, k0 is an integer between 1 and 10^9, _ is t-1, stdin is empty, c is equal to n, ans is a list containing n elements which are k0 - sum(ans) and 1 << i for all i in arr, l1 is a list containing two integers n and k. The length of ans is now equal to n, and the elements of ans which are all k0 - sum(ans) are being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. For each test case, it generates a list of n elements, where the first n-1 elements are powers of 2 corresponding to the binary representation of k, and the last element is the difference between k and the sum of the previous elements. The function then prints this list. The function repeats this process for all test cases, until the input is exhausted.

