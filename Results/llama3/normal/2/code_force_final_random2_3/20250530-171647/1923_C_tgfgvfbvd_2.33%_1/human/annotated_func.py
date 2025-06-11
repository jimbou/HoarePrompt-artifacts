#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two integers, and then a list of integers. The first integer is the number of test cases. The two integers are the length of the array and the number of queries. The list of integers is the array. Each query contains two integers: the borders of the subarray.
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
        
    #State: n is an integer equal to 0, m is equal to 0, l is an empty list, p is a list containing the cumulative sum of all integers in the list l, c is equal to the sum of all integers in the list l, _ is m, x is undefined, a is an integer equal to the first input, b is an integer equal to the second input, s is undefined, stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing an integer, two integers, and a list of integers. It calculates the cumulative sum of the list and then processes a number of queries, each containing two integers representing the borders of a subarray. For each query, it checks if the sum of the subarray is greater than or equal to twice the length of the subarray and prints 'YES' if true, 'NO' otherwise. The function repeats this process for all test cases and then terminates, leaving the input variables in a state where all lists are empty and all integers are 0, with standard input being empty.

