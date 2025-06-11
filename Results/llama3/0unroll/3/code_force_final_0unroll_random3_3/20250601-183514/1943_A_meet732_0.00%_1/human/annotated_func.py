#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The output state will contain multiple lines, each representing the result of a test case. For each test case, the output will be a single integer, which is the smallest index j such that the count of j in the array a is less than 2, or 0 if no such index exists. The output will be in the same order as the input test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then finds and prints the smallest index j such that the count of j in the array is less than 2, or 0 if no such index exists. The output is in the same order as the input test cases.

