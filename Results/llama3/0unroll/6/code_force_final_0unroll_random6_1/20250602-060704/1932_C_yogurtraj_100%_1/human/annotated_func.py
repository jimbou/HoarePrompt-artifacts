#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: The output state is a list of integers, where each integer is the result of a modular multiplication of the corresponding element in the input list 'a' and the count of 'L's in the input string 't', modulo 'm'. The list is in reverse order, with the last element being the result of the modular multiplication of the last element in 'a' and the count of 'L's in 't', modulo 'm'.

#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the results. Each test case consists of two integers (n and m), a list of n integers (a), and a string (t) of length n containing 'L' and 'R' characters. The function calculates the modular multiplication of each element in the list 'a' and the count of 'L's in the string 't', modulo 'm', and prints the results in reverse order. The function handles cases where the last character in the string 't' is either 'L' or 'R', and it correctly calculates the modular multiplication for each element in the list 'a' based on the corresponding character in the string 't'.

