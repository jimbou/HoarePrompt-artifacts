#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second and third lines contain two strings s and f of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise.
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
        
    #State: The number of cats that need to be moved from one box to another to make the number of cats in each box equal, for each test case.

#Overall this is what the function does:Calculates and prints the minimum number of cats that need to be moved from one box to another to equalize the number of cats in each box for each test case, considering multiple test cases from standard input.

