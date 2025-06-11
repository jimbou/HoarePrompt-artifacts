#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of two integers n and m, followed by two binary strings a and b of lengths n and m respectively.
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: The output state is the number of test cases `a` is the same as the initial state, stdin is empty, and the output contains `a` integers, each representing the maximum number of characters that can be matched between the two binary strings `a` and `b` in each test case.

#Overall this is what the function does:The function reads a number of test cases from standard input, where each test case consists of two integers and two binary strings. It then calculates the maximum number of characters that can be matched between the two binary strings in each test case and prints this number for each test case. The function does not modify the input strings or integers, and it does not store any information from the test cases after processing each one. After all test cases have been processed, the function terminates, leaving the input stream empty and the output containing the maximum match counts for each test case.

