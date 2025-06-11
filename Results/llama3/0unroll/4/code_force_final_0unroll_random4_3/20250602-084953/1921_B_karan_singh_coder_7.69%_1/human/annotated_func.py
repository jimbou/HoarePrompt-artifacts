#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a positive integer n (1 <= n <= 10^5). The second and third lines contain two strings s and f of length n, consisting of characters '0' and '1'.
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
        
    #State: The output state will contain the results of the loop's execution for each test case. For each test case, if the number of '1's in the strings s and t are equal, the output will be the number of '1's in s if the strings are not identical, otherwise it will be 0. If the number of '1's in s and t are not equal, the output will be the difference between the number of '1's in s and t, plus the number of positions where the strings differ, divided by 2.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a positive integer n and two binary strings s and t of length n. For each test case, it calculates the number of '1's in both strings and the number of positions where the strings differ. If the number of '1's in both strings is equal, it outputs the number of '1's in s if the strings are not identical, otherwise it outputs 0. If the number of '1's in the strings is not equal, it outputs the difference between the number of '1's in s and t, plus the number of positions where the strings differ, divided by 2. The function returns the results of all test cases as output.

