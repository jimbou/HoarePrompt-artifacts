#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m respectively.
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
        
    #State: Output State: The loop will execute 'a' number of times, where 'a' is an integer between 1 and 10^4 (inclusive). In each iteration, it will read two integers 'b' and 'c', and two binary strings 'd' and 'e' from the standard input. It will then find the maximum number of characters in 'd' that can be matched with characters in 'e' in order, and print this number. The state of 'a' remains unchanged after the loop execution.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers and two binary strings. It then finds the maximum number of characters in the first binary string that can be matched with characters in the second binary string in order, and prints this number for each test case. The function does not modify the input values and only produces output based on the provided test cases.

