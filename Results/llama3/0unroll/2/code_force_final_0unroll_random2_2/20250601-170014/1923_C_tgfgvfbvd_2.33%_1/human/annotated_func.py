#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of two integers, and then a space-separated list of integers. The first integer represents the number of test cases. The first integer in the list of two integers represents the length of the array c and the second integer represents the number of queries. The list of integers represents the array c. Each query is represented by a space-separated list of two integers, the borders of the subarray.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: The output state will be a series of 'YES' or 'NO' strings, each corresponding to a query in the input. The number of 'YES' or 'NO' strings will be equal to the total number of queries across all test cases. The 'YES' or 'NO' strings will be printed one per line, with no extra spaces or formatting.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer, a list of two integers, and a list of integers. It calculates the cumulative sum of the list of integers and then answers a series of queries, each represented by two integers (the borders of a subarray). For each query, it checks if the sum of the subarray is greater than or equal to twice the length of the subarray and prints 'YES' if true, 'NO' otherwise. The function outputs a series of 'YES' or 'NO' strings, one per query, with no extra formatting.

