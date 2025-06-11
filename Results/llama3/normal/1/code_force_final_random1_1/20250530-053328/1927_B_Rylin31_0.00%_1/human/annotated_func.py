#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for i in range(int(input())):
        l = int(input())
        
        array = list(map(int, input().split()))
        
        alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        rev_array = array[::-1]
        
        ans = []
        
        for j in range(l):
            ans.append(alp[rev_array[j:].count(rev_array[j]) - 1])
        
        print(''.join(map(str, ans)))
        
    #State: `i` is `t`, `stdin` is empty, `l` is an integer between 1 and 10^4, `array` is a list of integers, `alp` is a list of lowercase English letters, `rev_array` is a reversed copy of `array`, `ans` is a list containing the (count of `rev_array[j]` in `rev_array[j:]` - 1)th lowercase English letter for all `j` in range `l`, `j` is `l-1`, and a string of length `l` consisting of lowercase English letters is being printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints a string of lowercase English letters. It accepts a series of test cases, where each test case consists of an integer n followed by a list of n integers. The function reverses the list of integers, counts the occurrences of each integer in the reversed list, and maps these counts to corresponding lowercase English letters. It then prints a string composed of these letters. The function processes all test cases and prints the resulting strings.

