#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n). The array a is beautiful, i.e., it can be made all its elements the same by using the given operation an arbitrary number of times.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: The loop will execute t times, and for each execution, it will read two lines from stdin. The first line will contain a single integer n, and the second line will contain n integers. The loop will then process these integers and print the minimum count of consecutive equal elements in the array. The value of t will be decremented by 1 after each execution, and the loop will terminate when t becomes 0. The final state will have the same value of t (which will be 0), and the stdin will be empty. The output will contain t lines, each containing the minimum count of consecutive equal elements for the corresponding test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains a single integer n, and the second line contains n integers. It then processes these integers to find the minimum count of consecutive equal elements in the array and prints this count for each test case. If the array already contains all equal elements, it prints -1. The function continues this process until all test cases have been read and processed, at which point the standard input is empty and the output contains the minimum count of consecutive equal elements for each test case.

