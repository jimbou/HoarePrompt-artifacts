#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n, then two lists a and b of length n. a and b are lists of non-decreasing positive integers less than or equal to 10^9.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: The number of elements in b that are less than the corresponding elements in a, for each test case, minus one test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two lists a and b of length n. It then calculates and prints the number of elements in list b that are less than the corresponding elements in list a, minus one test case.

