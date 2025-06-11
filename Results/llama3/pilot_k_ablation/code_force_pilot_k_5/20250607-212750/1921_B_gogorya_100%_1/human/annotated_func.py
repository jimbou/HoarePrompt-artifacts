#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains a single integer n (1 ≤ n ≤ 10^5). The second and third lines contain strings s and f of n characters, where each character is either '1' or '0'.
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
        
    #State: t is 0, n is an integer greater than or equal to 0, s1 is a string, s2 is a string, res is the absolute difference between the number of '1's in s1 and s2, _ is t, i is n, hd is the Hamming distance between s1 and s2, and stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an integer n, and two strings s1 and s2 of length n containing only '1's and '0's. For each test case, it calculates the absolute difference between the number of '1's in s1 and s2, and the Hamming distance between s1 and s2. It then prints the sum of the absolute difference and half of the absolute difference between the Hamming distance and the absolute difference. After processing all test cases, the function leaves the input stream empty.

