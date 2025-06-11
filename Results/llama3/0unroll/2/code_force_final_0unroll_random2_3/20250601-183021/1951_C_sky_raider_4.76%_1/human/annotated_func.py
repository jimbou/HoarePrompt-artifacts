#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3*10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The output state will contain multiple lines of output, each representing the result of a test case. Each result is the minimum cost to make all elements in the array equal, considering the constraints of the problem. The cost is calculated by summing the product of each element and the minimum of m and k, and subtracting the sum of squares of the minimum of m and k divided by 2. The output state will be a series of integers, each representing the minimum cost for a test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers (n, m, k) and a list of n integers. It calculates the minimum cost to make all elements in the list equal, considering the constraints of the problem, and prints the result for each test case. The cost is calculated by summing the product of each element and the minimum of m and k, and subtracting the sum of squares of the minimum of m and k divided by 2. The function outputs a series of integers, each representing the minimum cost for a test case.

