#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
    for ii in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        t = input()
        
        l = t.count('L')
        
        k = 0
        
        q1 = 0
        
        q2 = 0
        
        if t[-1] == 'L':
            k = a[l - 1] % m
            q1 = l - 2
            q2 = l
        else:
            k = a[l] % m
            q1 = l - 1
            q2 = l + 1
        
        y = str(k)
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y += ' ' + str(k)
        
        print(y[::-1])
        
    #State: n is an integer greater than or equal to 0, m is an integer, a is a list of integers, t is a string, l is the number of 'L' characters in t, y is the string representation of k followed by a space and the updated string representation of k n-2 times, i is -n+1, q1 and q2 are integers, k is an integer that has been updated based on the values of t[i], q1, q2, a[q1], a[q2], and m, and the reverse of the string y is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers (n and m), a list of n integers (a), and a string (t) of length n containing 'L' and 'R' characters. It then processes the test case by iterating over the string t in reverse order, updating an integer k based on the characters in t and the corresponding values in a, and appending the updated k to a string y. Finally, it prints the reverse of the string y. The function repeats this process for each test case.

