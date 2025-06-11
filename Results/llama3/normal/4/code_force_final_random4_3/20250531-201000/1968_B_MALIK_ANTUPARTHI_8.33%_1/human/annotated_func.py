#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
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
        
    #State: a is an integer between 1 and 10^4 (inclusive), b is an integer, c is an integer, d is a binary string of length b, e is a binary string of length c, i is equal to a, j is equal to b, k is equal to b, and the value of k which is equal to b is being printed, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers and two binary strings. It then finds the maximum number of characters that can be matched between the two binary strings by iterating through the first string and finding the index of each character in the second string. The function prints the maximum number of matched characters for each test case.

