#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0, n is an integer, i is n, T is a list of integers, a is a list containing the integers 1000 and the cumulative sum of the first n-1 elements of T, and the string representation of the elements in a which is "1000 [1000 + cumulative sum of the first n-1 elements of T]" has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains an integer n, and the second line contains n-1 integers. It then calculates the cumulative sum of these integers, starting from 1000, and prints the resulting list of integers. The function continues this process until all test cases have been processed.

