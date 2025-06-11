#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t test cases. Each test case consists of two lines. The first line contains an integer n (2 <= n <= 500), and the second line contains n-1 integers x_2, x_3, ..., x_n (1 <= x_i <= 500).
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
        
    #State: The loop will print the cumulative sum of the input integers for each test case, with the first element being 1000.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n-1 integers. It then calculates the cumulative sum of these integers, starting with an initial value of 1000, and prints the resulting sequence for each test case.

