#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three inputs: first an integer, then two integers, and then a list of integers. The list of integers is followed by a number of queries, each query consisting of two integers.
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
        
    #State: n is an integer equal to the first integer from the input, m is 0, l is a list of integers, p is a list containing the cumulative sum of all integers in the list l, c is equal to the sum of all integers in the list l, _ is m, a is an integer equal to the last integer from the input, b is an integer equal to the last integer from the input, s is the cumulative sum of all integers in the original list up to index b - 1, x is the last integer in the list l. If a - 2 >= 0, s is the cumulative sum of all integers in the original list up to index b - 1 minus the cumulative sum of all integers in the original list up to index a - 2. Otherwise, s is the cumulative sum of all integers in the original list up to index b - 1. If b - a + 1 > 1 and s >= 2 * (b - a + 1), then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer, two integers, and a list of integers, followed by a number of queries. It calculates the cumulative sum of the list of integers and then answers queries by determining if the sum of a specified sub-range of the list is greater than or equal to twice the length of the sub-range. The function prints 'YES' if the condition is met and 'NO' otherwise.

