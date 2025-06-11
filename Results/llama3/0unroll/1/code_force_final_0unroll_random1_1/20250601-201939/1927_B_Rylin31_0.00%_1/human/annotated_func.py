#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the lost string. The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n) — the trace of the string.
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
        
    #State: The output state is a string of characters, where each character is the (count of the corresponding number in the reversed array - 1)th letter of the alphabet. The string is constructed by iterating over the reversed array and appending the corresponding character to the result string. The output state is the result string after all iterations of the loop have finished.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains the length of the lost string, and the second line contains a list of integers representing the trace of the string. It then constructs a string by iterating over the reversed list of integers, appending a character to the result string based on the count of each integer in the reversed list. The character is determined by the count of the integer minus one, which corresponds to a letter in the alphabet. The function prints the resulting string for each test case.

