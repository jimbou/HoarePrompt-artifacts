#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The loop has finished executing, and the output state is the final state of the variables after all iterations.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then finds the smallest positive integer that is not present in the input sequence or the smallest positive integer that appears only once in the sequence, and prints this integer. If no such integer is found, it prints 0. The function processes all test cases and prints the corresponding results.

