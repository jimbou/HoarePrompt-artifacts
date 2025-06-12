#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: stdin is empty, `t` is an integer (1 <= t <= 10^4), `n` is an integer (1 <= n <= 2*10^5), `m` is an integer (1 <= m <= 10^4), `arr` is a list of integers, `s` is a string, `l` is `n`, `r` is -1, `_` is `t`, `p` is 1, `ans` is a list of integers, each being the product of the elements of `arr` at indices `r` and `l` modulo `m` for each character in `s` in reverse order.

#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the results. For each test case, it reads two integers (n and m), a list of n integers (arr), and a string (s) of length n. It then calculates the product of elements in arr at specific indices (determined by the characters in s) modulo m, and prints the results in reverse order. The function consumes all input from stdin and produces output for each test case.

