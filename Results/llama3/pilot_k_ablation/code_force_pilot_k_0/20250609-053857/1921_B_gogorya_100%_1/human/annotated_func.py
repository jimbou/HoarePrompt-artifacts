#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        hd = 0
        
        for i in range(n):
            if s1[i] != s2[i]:
                hd += 1
        
        res = abs(s1.count('1') - s2.count('1'))
        
        print(res + abs(hd - res) // 2)
        
    #State: The number of operations required to make the initial and final state of the boxes the same for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the number of boxes, the initial state of the boxes (as a string of '1's and '0's), and the desired state of the boxes (as a string of '1's and '0's). It then calculates and prints the minimum number of operations required to transform the initial state into the desired state for each test case.

