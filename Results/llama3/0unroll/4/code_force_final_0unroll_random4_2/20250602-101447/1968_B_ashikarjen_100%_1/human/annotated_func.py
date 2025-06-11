#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: Output State: The value of k will be the length of the longest common substring of a and b, and the value of j will be the index of the character in b that is one position after the last character of the longest common substring. The values of t, n, m, a, and b remain unchanged.
    print(k)
    #This is printed: the length of the longest common substring of strings a and b
    return
    #The program returns the length of the longest common substring of strings 'a' and 'b' and the index of the character in string 'b' that is one position after the last character of the longest common substring. The values of variables 't', 'n', 'm', 'a', and 'b' remain unchanged.

#Overall this is what the function does:This function takes two binary strings 'a' and 'b' as input and returns the length of the longest common substring of 'a' and 'b'. The function does not modify the input strings or any other variables. It only reads the input strings and prints the length of the longest common substring. The function does not perform any other actions or modifications.

