#State of the program right berfore the function call: stdin contains a number of test cases, and for each test case, it contains an integer n followed by a list of n non-negative integers.
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The output state will be a string of characters, where each character is the (j+1)th letter of the alphabet, and the number of times each character appears is equal to the number of times its corresponding index appears in the input array. For example, if the input array is [1, 2, 2, 3, 3, 3], the output string will be "bcbbcc".

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n non-negative integers. For each test case, it generates a string where each character is the (j+1)th letter of the alphabet, and the number of times each character appears is equal to the number of times its corresponding index appears in the input array. The function then prints the generated string for each test case.

