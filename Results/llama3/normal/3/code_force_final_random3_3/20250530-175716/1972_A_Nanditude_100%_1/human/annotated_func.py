#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (1 <= n <= 100), then two lists a and b of length n, each containing non-negative integers in non-decreasing order.
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
        
    #State: t is 0, n is an integer greater than or equal to 0, a is a list of integers, b is a list of integers, cnt is an integer between 0 and n, i is an integer between 0 and n, j is n-1, stdin is empty, and the value of cnt which is the number of elements in list b that are less than the corresponding elements in list a is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and two lists a and b of length n. It then counts the number of elements in list b that are less than the corresponding elements in list a and prints this count. The function repeats this process for all test cases and finally empties the standard input.

