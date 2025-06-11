#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and a string s consisting of n characters 'L' and 'R'.
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
        
    #State: n is an integer that must be at least 3, m is an integer, a is a list of integers, t is a string, l is an integer equal to the number of 'L' characters in t, y is a list of n integers where all elements are 0 except the last n - 1 elements which are k * a[q] % m, k is k * a[q] % m, q is either q1 or q2, q1 is either l - 2, l - 3, or l - 1, q2 is either l, l + 1, or l + 2, ii is t - 1, stdin is empty, i is -1, and if t[i] is 'R' then q is q2, otherwise q is q1, and the elements of y are printed, y (where y is a list of n integers where all elements are 0 except the last n - 1 elements which are k * a[q] % m)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It reads an integer t, followed by t test cases. Each test case consists of two integers n and m, n integers a_1 to a_n, and a string s of n characters 'L' and 'R'. The function calculates a list y of n integers based on the input and prints the elements of y. The calculation involves iterating over the string s from right to left, updating the value of k based on the characters in s and the corresponding values in the list a, and storing the updated k values in the list y. The function repeats this process for each test case and prints the resulting list y for each case.

