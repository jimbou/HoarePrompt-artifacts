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
        
    #State: a is an integer between 1 and 10^4 (inclusive), i is equal to a, b is an integer between 1 and 2 * 10^5 (inclusive), c is an integer between 1 and 2 * 10^5 (inclusive), d is a binary string of length b, e is a binary string of length c, j is equal to b, and k is equal to the minimum of b and c, and the minimum of b and c is being printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum of two values. It first reads an integer t, then for each test case, it reads two integers n and m, and two binary strings a and b. It then iterates through the first binary string and checks if each character is present in the second binary string. If it is, it updates a counter k to the index of the character in the second string plus one. If the character is not found or if the end of the first string is reached, it breaks the loop. Finally, it prints the value of k, which is the minimum of the length of the first binary string and the length of the second binary string.

