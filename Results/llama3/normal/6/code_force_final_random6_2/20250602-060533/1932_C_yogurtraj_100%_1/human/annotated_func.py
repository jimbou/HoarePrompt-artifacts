#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), then t test cases. Each test case contains three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
        y = [0] * n
        
        y[-1] = k
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y[i] = k
        
        print(*y)
        
    #State: n is an integer, m is an integer, a is a list of integers, t is a string, l is the number of 'L' characters in t, y is a list of n integers where y[i] is k * a[q1] % m for all i except the last one which is k, ii is t, q1 and q2 are integers, k is an integer. If the last character of t is 'L', then q1 is 0, q2 is l, and k is the remainder of a[l - 1] divided by m. Otherwise, q1 is -1, q2 is l + 1, and k is a[l] % m., and the elements of the list y are printed, which are k * a[q1] % m for all i except the last one which is k

#Overall this is what the function does:This function reads input from standard input, processes it, and prints the results. It expects the input to contain an integer t, followed by t test cases. Each test case consists of three lines: two integers n and m, a list of n integers a, and a string t of length n containing 'L' and 'R' characters. The function calculates a list y of n integers based on the input values and prints the elements of y. The calculation involves iterating over the string t from right to left, updating values based on the characters in t and the corresponding values in a, and applying modulo operations with m. The final state of the program is that the calculated list y is printed, and the input values are not modified.

