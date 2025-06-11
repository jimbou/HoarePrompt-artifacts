#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains a single integer n (1 <= n <= 10^5), the second line contains a string s of n characters where each character is either '1' or '0', and the third line contains a string f of n characters where each character is either '1' or '0'.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: `n` is an integer greater than or equal to 0, `s` is a string, `t` is a string, `s1` is the number of '1' characters in `s`, `t1` is the number of '1' characters in `t`, `cnt` is the number of positions where `s` and `t` differ, `_` is equal to the number of test cases, stdin is empty. If `s1` equals `t1`, the number of '1' characters in `s` is printed if `s` and `t` differ in at least one position, otherwise 0 is printed. If `s1` does not equal `t1`, the minimum number of operations required to make `s` and `t` equal is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an integer n, a string s of n characters, and a string t of n characters. It then calculates the number of '1' characters in s and t, and the number of positions where s and t differ. If the number of '1' characters in s and t are equal, it prints the number of '1' characters in s if s and t differ in at least one position, otherwise it prints 0. If the number of '1' characters in s and t are not equal, it prints the minimum number of operations required to make s and t equal. The function processes all test cases and prints the results for each case.

