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
        
    #State: The output state will contain the results of all the test cases, where each result is either 'YES' or 'NO', indicating whether the sum of the subarray from index a to b is greater than or equal to twice the length of the subarray. The results will be printed in the order they were processed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer, a list of two integers, and a list of integers, followed by a list of queries. For each query, it calculates the sum of a subarray within the list of integers and checks if it is greater than or equal to twice the length of the subarray. The function then prints 'YES' if the condition is met and 'NO' otherwise, for each query in the order they were processed.

