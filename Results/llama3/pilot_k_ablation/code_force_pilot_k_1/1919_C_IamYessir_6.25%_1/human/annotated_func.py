#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the size of the array) and then a list of integers (the elements of the array). The size of the array is a positive integer and the elements of the array are positive integers less than or equal to the size of the array.
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: `stdin` is empty, `n` is not defined, `lit` is not defined, `a` is not defined, `b` is not defined, `cp` is not defined, `s` is not defined, `_` is the number of test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the size of the array) followed by a list of integers (the elements of the array). It then processes each test case by splitting the array into two lists (a and b) based on the condition that elements in list a are in increasing order and elements in list b are also in increasing order. The function counts the number of pairs of adjacent elements in both lists that are in increasing order and prints this count for each test case. After processing all test cases, the function leaves the standard input empty and does not return any value.

