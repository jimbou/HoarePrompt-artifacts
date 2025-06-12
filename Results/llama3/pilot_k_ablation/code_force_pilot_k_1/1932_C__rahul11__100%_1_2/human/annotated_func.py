#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and a string s consisting of n characters 'L' and 'R'.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = input()
        
        l = 0
        
        r = n - 1
        
        for k in s:
            if k == 'L':
                l += 1
            else:
                r -= 1
        
        p = 1
        
        ans = []
        
        for strr in s[::-1]:
            if strr == 'R':
                r += 1
                p = p * arr[r] % m
            else:
                l -= 1
                p = p * arr[l] % m
            ans.append(p)
        
        print(*ans[::-1])
        
    #State: stdin is empty, t is undefined, n is undefined, m is undefined, arr is undefined, s is undefined, l is undefined, r is undefined, p is undefined, ans is undefined.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints the result. It accepts a series of test cases, each consisting of two integers (n and m), an array of n integers, and a string of n characters ('L' and 'R'). The function then performs a series of operations on the input data, including iterating through the string, updating indices, and calculating a product modulo m. Finally, it prints the result of these operations in reverse order. The function does not return any value, and its execution leaves the input variables undefined.

