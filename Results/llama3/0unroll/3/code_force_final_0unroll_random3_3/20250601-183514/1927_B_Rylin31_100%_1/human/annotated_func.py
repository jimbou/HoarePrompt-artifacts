#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains two lines of input. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The output state will be a series of strings, each representing the output for a test case. Each string will consist of lowercase English letters, where the frequency of each letter is determined by the input array. Specifically, for each input array, the output string will have the same length as the array, and the i-th character of the string will be the (array[i]+1)-th letter of the alphabet (where 'a' is the 1st letter, 'b' is the 2nd letter, and so on). The strings will be separated by newline characters.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It then generates a string for each test case, where the i-th character of the string corresponds to the (array[i]+1)-th letter of the alphabet, with the frequency of each letter determined by the input array. The function prints each generated string on a new line, resulting in a series of strings as output.

