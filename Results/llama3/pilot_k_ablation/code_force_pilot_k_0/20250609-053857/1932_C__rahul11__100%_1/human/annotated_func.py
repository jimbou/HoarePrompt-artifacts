#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and a string s of length n consisting of 'L' and 'R' characters.
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
        
    #State: The output state will be a list of integers, where each integer is the product of the elements in the array `arr` at the indices specified by the string `s`, taken in reverse order, modulo `m`. The list will have the same length as the string `s`.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers (n and m), a list of n integers, and a string of length n containing 'L' and 'R' characters. It then processes the string in reverse order, calculating the product of the elements in the list at the indices specified by the string, modulo m, and outputs the results as a list of integers.

