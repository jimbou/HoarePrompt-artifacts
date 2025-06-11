#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains a single integer n (3 <= n <= 10^5).
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: n is 0, i is t, p is a list of n integers where every other element starting from the first is n-2, n-4, n-6, and so on, and the rest are zeros except for the odd-indexed elements which are 1, 3, 5, ..., n-1, ind is n, stdin contains no lines of input, and the list p is not being printed

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of an array. For each test case, the function generates an array of size n, where every other element starting from the first is assigned a value from the sequence n-2, n-4, n-6, ..., and the remaining elements are assigned values from the sequence 1, 3, 5, ..., n-1. The function then prints each generated array. After processing all test cases, the function concludes, leaving the input stream empty.

