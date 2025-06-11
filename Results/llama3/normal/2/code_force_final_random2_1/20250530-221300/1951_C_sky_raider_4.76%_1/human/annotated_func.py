#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: i is equal to the number of test cases minus 1, n is equal to 0, m is an integer, k is an integer equal to its original value minus n times the minimum of m and k, l is a sorted list of integers, s is the minimum of m and k, c is k squared divided by 2 plus the sum of the products of the first n elements of l and the minimum of m and k minus the sum of the squares of the minimum of m and k divided by 2, stdin contains no test cases, and the integer value of c is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each consisting of two lines. The first line contains three integers n, m, and k, and the second line contains n integers. It sorts the integers, calculates a value c based on the sorted integers, the minimum of m and k, and the sum of squares of the minimum of m and k, and prints the integer value of c. The function repeats this process for all test cases, consuming all input from standard input.

