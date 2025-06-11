#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first three space-separated integers n, k, and q, and then k space-separated integers a_i, and then k space-separated integers b_i, and finally q space-separated integers d. n and k are positive integers, q is a non-negative integer, a_i and b_i are positive integers, and d are non-negative integers.
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
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: The output state is a series of q integers, each representing the value of m, which is calculated based on the input values of n, k, q, a, b, and d. The values of n, k, and q are not changed, and the values of a, b, and d are used to calculate the values of ad, bd, and v, which are then used to calculate the values of m. The output state is a series of q integers, each representing the value of m, which is calculated based on the input values of n, k, q, a, b, and d.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four inputs: n, k, q, a_i, b_i, and d. It calculates the differences between consecutive elements in a_i and b_i, and then uses these differences to calculate the value of m for each query in d. The function prints the calculated values of m for each query in each test case.

