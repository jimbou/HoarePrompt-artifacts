#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 space-separated integers x_2, x_3, ..., x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0, and the standard output contains multiple lines. Each line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 1000), where a_i = 1000 - (x_2 + x_3 + ... + x_i).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a number of integers, and for each test case, it calculates and prints a sequence of integers to standard output. The sequence is calculated by starting with 1000 and subtracting each input integer from the previous value, and the resulting sequence is printed in reverse order.

