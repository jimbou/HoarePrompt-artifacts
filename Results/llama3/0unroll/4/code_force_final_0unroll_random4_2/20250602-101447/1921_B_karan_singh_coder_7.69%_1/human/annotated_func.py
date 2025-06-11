#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains an integer n, followed by two strings s and f of length n, consisting of '0' and '1' characters.
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
        
    #State: The output state will contain t lines, each representing the result of a test case. For each test case, if the number of '1's in strings s and t are equal, the output will be the number of '1's in s if the strings are not identical, otherwise it will be 0. If the number of '1's in s and t are not equal, the output will be the difference between the number of '1's in s and t, plus the number of positions where s and t differ, divided by 2.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result of each test case. For each test case, it compares two binary strings s and t of equal length, counts the number of '1's in each string, and calculates the number of positions where the strings differ. If the number of '1's in s and t are equal, it prints the number of '1's in s if the strings are not identical, otherwise it prints 0. If the number of '1's in s and t are not equal, it prints the difference between the number of '1's in s and t, plus the number of positions where s and t differ, divided by 2. The function does not modify the input strings or any external state, and its output is solely based on the input provided.

