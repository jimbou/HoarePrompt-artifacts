#State of the program right berfore the function call: **stdin contains multiple test cases. Each test case consists of three parts:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: Output State: The loop will execute for a specified number of test cases. For each test case, it will process a list of integers and answer a series of queries. The output will be a series of 'YES' or 'NO' strings, one for each query, indicating whether a certain condition is met. The condition is that the number of 1s in a subarray is greater than or equal to the difference between the sum of the subarray and its length. The output will be printed to the console.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of a list of integers and a series of queries. For each query, it checks if the number of 1s in a specified subarray is greater than or equal to the difference between the sum of the subarray and its length, and prints 'YES' or 'NO' to the console accordingly.

