#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: n is 0, m is an integer, k is an integer equal to its original value minus n times the minimum of m and k, l is a sorted list of integers, s is the minimum of m and k, c is k * k / 2 plus the sum of l[i] times the minimum of m and k minus the square of the minimum of m and k divided by 2 for i in range(n), i is n-1, stdin contains no lines of input, and this is printed: the integer value of c which is equal to k * k / 2.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, m, and k, and the second line contains n integers. The function sorts the integers, calculates a value c based on the sorted integers and the minimum of m and k, and prints the integer value of c. The function repeats this process for all test cases in the input.

