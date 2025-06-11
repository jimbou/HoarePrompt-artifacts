#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains two positive integers n and m. The second line contains a binary string a of length n. The third line contains a binary string b of length m.
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: The value of variable 'a' remains unchanged as an integer. The stdin is empty as all the test cases have been consumed by the loop. The loop has printed the value of variable 'k' for each test case, which represents the maximum number of characters that can be matched between strings 'd' and 'e' in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers and two binary strings. It then finds the maximum number of characters that can be matched between the two binary strings in each test case and prints this value for each test case. The function consumes all test cases from standard input and leaves it empty.

