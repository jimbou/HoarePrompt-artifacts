#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), then t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: The output state is a string of integers separated by spaces, where each integer is the result of a modular multiplication operation. The number of integers in the output string is equal to the number of test cases (t). Each integer is calculated by multiplying the corresponding element in the input array (a) with the previous result, modulo m, and the direction of the multiplication is determined by the corresponding character in the input string (s). The output string is in reverse order of the input string.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts a series of test cases, where each test case consists of two integers (n and m), an array of n integers (a), and a string of n characters (s). The function performs modular multiplication operations based on the input array and string, and prints the results as a string of integers separated by spaces. The output string is in reverse order of the input string. The function does not return any value, but instead prints the output directly to standard output.

