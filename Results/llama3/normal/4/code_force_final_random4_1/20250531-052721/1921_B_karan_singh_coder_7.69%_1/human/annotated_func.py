#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two strings of the same length as the integer. The strings consist of '1's and '0's. The sum of the lengths of the strings over all test cases does not exceed 10^5.
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
        
    #State: All test cases have been processed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It calculates the minimum number of operations required to make the two strings identical, considering the difference in the count of '1's between the strings, and prints the result for each test case.

