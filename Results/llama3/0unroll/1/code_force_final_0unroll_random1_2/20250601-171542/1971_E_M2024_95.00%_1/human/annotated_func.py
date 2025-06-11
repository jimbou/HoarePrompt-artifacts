#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first a line with three integers n, k, and q, then a line with k integers a_i, then a line with k integers b_i, and finally q lines each with a single integer d. n, k, and q are integers such that 1 <= k <= n <= 10^9 and 1 <= q <= 10^5. a_i and b_i are strictly increasing sequences of integers such that 1 <= a_i <= n and 1 <= b_i <= 10^9. d is an integer such that 0 <= d <= n.
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        
        a = [0] + list(map(int, input().split()))
        
        b = [0] + list(map(int, input().split()))
        
        ad = [0]
        
        bd = [0]
        
        for i in range(1, len(a)):
            ad.append(a[i] - a[i - 1])
        
        for i in range(1, len(b)):
            bd.append(b[i] - b[i - 1])
        
        v = [0]
        
        for i in range(1, len(a)):
            v.append(ad[i] / bd[i])
        
        for l in range(q):
            m = 0
            i = 1
            ql = int(input())
            s = bisect_left(a, ql)
            if a[s] == ql:
                print(b[s], end=' ')
                continue
            ql -= a[s - 1]
            m += b[s - 1]
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: The loop has executed all the iterations, and the output state is the final state of the variables after the last iteration. The variable 't' is still an integer, but its value has been decremented by 1 for each iteration of the loop. The stdin contains no more test cases. The variables 'n', 'k', 'q', 'a', 'b', 'ad', 'bd', 'v', 'm', 'i', 'ql', and 's' have been updated with the values from the last test case. The variable 'm' holds the final calculated value for the last query in the last test case. The variable 'i' is still 1, and 'ql' and 's' hold the values from the last query in the last test case. The variable 'v' holds the calculated values for the last test case. The variables 'ad' and 'bd' hold the differences between consecutive elements in 'a' and 'b' respectively, for the last test case. The variable 'b' holds the last calculated value for the last query in the last test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four inputs: three integers n, k, and q, followed by k integers a_i, k integers b_i, and q integers d. It calculates the differences between consecutive elements in a_i and b_i, and then for each query d, it finds the corresponding value in b_i by interpolating between the closest elements in a_i and b_i. The function prints the calculated values for each query, separated by spaces, and then prints a newline character after each test case. The function continues this process until all test cases have been read from standard input.

