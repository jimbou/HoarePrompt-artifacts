#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second and third lines contain strings s and f of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The sum of n over all test cases does not exceed 10^5.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: The number of cats that need to be moved to make the number of cats in each box equal, for each test case, is printed to the console. The input buffer is empty after reading all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an integer n, and two strings s and f of length n. It calculates the minimum number of cats that need to be moved to make the number of cats in each box equal, and prints this number to the console for each test case. The function processes all test cases and empties the input buffer.

