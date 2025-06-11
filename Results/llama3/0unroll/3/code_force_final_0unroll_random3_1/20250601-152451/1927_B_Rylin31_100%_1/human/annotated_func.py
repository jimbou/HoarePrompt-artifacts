#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n. The second line contains n non-negative integers.
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The output state will contain multiple lines, each representing the output for a test case. Each line will contain a string of lowercase English letters, where the frequency of each letter is determined by the input array. Specifically, the i-th letter in the string will be the (array[i] + 1)-th occurrence of the letter corresponding to the index array[i] in the alphabet (with 'a' corresponding to index 0, 'b' to index 1, and so on). The length of each string will be equal to the length of the input array.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by n non-negative integers. For each test case, it generates a string of lowercase English letters based on the input array, where the frequency of each letter is determined by the array values. The function then prints the generated string for each test case.

