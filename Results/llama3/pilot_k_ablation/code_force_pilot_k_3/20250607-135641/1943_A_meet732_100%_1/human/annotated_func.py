#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: The loop has finished executing all iterations, stdin is empty, and the output is a list of integers, each representing the smallest positive integer missing from the corresponding input list.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds and prints the smallest positive integer missing from each list. If the list contains all positive integers from 1 to its length, it prints 0. The function processes all test cases and produces a list of integers as output, where each integer represents the smallest positive integer missing from the corresponding input list.

