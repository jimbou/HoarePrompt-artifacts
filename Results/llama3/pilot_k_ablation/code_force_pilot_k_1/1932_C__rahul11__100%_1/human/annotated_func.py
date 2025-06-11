#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: stdin is empty, `t` is an integer greater than or equal to 0, `n` is an integer greater than or equal to 0, `m` is an integer, `arr` is a list of integers, `s` is a string, `l` is -len(s) + n - 1, `r` is n - 1 + count of 'R' in s, `p` is the product of arr elements at indices from n-1 to n-1-len(s) (inclusive) and from n-1 to n-1 + count of 'R' in s (inclusive) modulo m, `ans` is a list containing len(s) elements which are the values of `p` after each iteration.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts a series of test cases, each consisting of two integers (n and m), a list of n integers, and a string of length n containing 'L' and 'R' characters. The function then calculates the product of certain elements in the list, modulo m, based on the string and prints the results in reverse order. The function continues this process until all test cases have been processed, at which point stdin is empty.

