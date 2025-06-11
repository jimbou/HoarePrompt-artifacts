#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first three integers n, k, and q, then a list of k integers a_i, then a list of k integers b_i, and finally q integers d. n and k are positive integers, q is a non-negative integer, 1 <= k <= n <= 10^9, 1 <= q <= 10^5, 1 <= a_i <= n, 1 <= b_i <= 10^9, a_i < a_{i+1} for every 1 <= i <= k-1, a_k = n, and b_i < b_{i+1} for every 1 <= i <= k-1. The sum of k over all test cases doesn't exceed 10^5, and the sum of q over all test cases doesn't exceed 10^5.
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
        
    #State: The loop has executed t times, and for each test case, it has calculated and printed the values of m for q queries. The values of n, k, q, a, b, ad, bd, and v have been updated for each test case. The final values of these variables are the values from the last test case. The values of t and stdin have not been changed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains four inputs: three integers n, k, and q, followed by a list of k integers a_i, a list of k integers b_i, and q integers d. It calculates and prints the values of m for q queries in each test case, where m is calculated based on the values of a, b, and the query value ql. The function processes t test cases and updates the values of n, k, q, a, b, ad, bd, and v for each test case. The final values of these variables are the values from the last test case. The function does not modify the values of t and stdin.

