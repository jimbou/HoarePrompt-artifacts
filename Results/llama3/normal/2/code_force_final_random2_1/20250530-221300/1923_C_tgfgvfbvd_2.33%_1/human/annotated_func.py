#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three inputs: first an integer, then a list of two integers, and then a list of integers. The list of integers is followed by a list of queries, where each query is a list of two integers.
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
        
    #State: The loop has finished executing all iterations, and the output state is the same as the initial state, with the addition of the cumulative sums of the elements in the list l, and the sum of all elements in the list l. The loop has also printed 'YES' or 'NO' for each query, depending on whether the cumulative sum of the elements in the list l from index a-1 to b-1 is greater than or equal to twice the difference between b and a plus 1.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer, a list of two integers, and a list of integers, followed by a list of queries. It calculates the cumulative sum of the list of integers and then processes each query by comparing the cumulative sum of the elements in the specified range to twice the range size. Based on this comparison, it prints 'YES' if the cumulative sum is greater than or equal to twice the range size, and 'NO' otherwise. The function does not modify the input state and only produces output based on the queries.

