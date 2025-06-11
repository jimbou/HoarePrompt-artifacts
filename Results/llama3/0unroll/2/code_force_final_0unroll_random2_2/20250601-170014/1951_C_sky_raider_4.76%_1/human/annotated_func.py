#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop will execute for a number of times equal to the number of test cases provided in the input. For each test case, it will calculate and print the value of c, which represents the total sum of the products of the elements in the sorted list l and their corresponding counts, minus the sum of the squares of the counts divided by 2. The output will be a series of integers, each representing the calculated value of c for a test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, each consisting of two lines: the first line contains three integers n, m, and k, and the second line contains n integers. For each test case, it sorts the integers, calculates a value c based on the sorted integers and the given parameters, and prints the calculated value. The function repeats this process for each test case provided in the input.

