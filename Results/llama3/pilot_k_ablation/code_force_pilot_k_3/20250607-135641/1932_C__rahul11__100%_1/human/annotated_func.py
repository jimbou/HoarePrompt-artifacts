#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), then t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: The loop head variable `_` is equal to the value of `t` from the initial state, `n` is an integer equal to the first input, `m` is an integer equal to the second input, `arr` is a list of integers from the third input, `s` is a string equal to the fourth input, `l` is equal to 0, `r` is equal to `n` - 1 minus the number of 'R' characters in `s` plus the number of 'R' characters in `s`, `p` is the product of the original value of `p` and the value of `arr` at index `r` modulo `m` if the first character of `s` is 'R', or the product of the original value of `p` and the element at index `l` in `arr`, modulo `m` if the first character of `s` is not 'R`, `ans` is a list containing the product of the original value of `p` and the value of `arr` at index `r` modulo `m` if the last character of `s` is 'R', or the product of the original value of `p` and the element at index `l` in `arr`, modulo `m` if the last character of `s` is not 'R`, and the product of the original value of `p` and the value of `arr` at index `r` plus 1 modulo `m` if the third last character in `s` is 'R', or the product of the original value of `p` and the element at index `l` in `arr`, modulo `m` if the third last character in `s` is not 'R`, and the value of `p`, `strr` is the first character in `s`, and the elements of `ans` in reverse order are being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m), a list of n integers, and a string of length n containing 'L' and 'R' characters. For each test case, it calculates the product of the integers at specific indices in the list, determined by the 'L' and 'R' characters in the string, modulo m. The function then prints the calculated products in reverse order for each test case.

