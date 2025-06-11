#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of two lines. The first line contains an integer n. The second line contains n-1 space-separated integers.
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
        
    #State: t = 0, n = None, line = None, T = None, a = None, result = None

#Overall this is what the function does:The function reads a number of test cases from standard input, processes each test case by reading an integer n and n-1 space-separated integers, calculates a list of cumulative sums, and prints the resulting list for each test case. The function does not return any value and only produces output through printing.

