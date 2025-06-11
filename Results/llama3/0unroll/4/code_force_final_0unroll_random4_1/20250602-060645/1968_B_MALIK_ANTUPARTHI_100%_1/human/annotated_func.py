#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
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
        
    #State: The loop has executed 'a' number of times, each time printing the maximum number of characters that can be matched between the two binary strings 'd' and 'e' from left to right, considering only the first occurrence of a character in 'e' for each character in 'd'. The values of 'a', 'b', 'c', 'd', and 'e' have been updated 'a' number of times, with 'b' and 'c' being the lengths of the strings 'd' and 'e' respectively, and 'd' and 'e' being the binary strings themselves. The variable 'k' has been reset to 0 at the beginning of each iteration and updated based on the matching characters. The stdin has been consumed 'a' number of times, with each consumption consisting of two integers and two binary strings.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers and two binary strings. It then finds the maximum number of characters that can be matched between the two binary strings from left to right, considering only the first occurrence of a character in the second string for each character in the first string. The function prints this maximum number of matched characters for each test case.

