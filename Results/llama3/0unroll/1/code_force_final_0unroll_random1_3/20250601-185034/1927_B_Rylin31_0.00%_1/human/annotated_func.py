#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n) — the trace of the string.
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
        
    #State: The output state is a string of characters, where each character is the (count of the corresponding number in the reversed array - 1)th letter of the alphabet. The string is constructed by iterating over the reversed array and appending the corresponding letter to the answer string. The output state is the concatenation of all the answer strings for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n followed by a line of n integers. It then processes each test case by reversing the array of integers, iterating over the reversed array, and appending a character to the answer string based on the count of the current number in the remaining reversed array. The character is determined by the count minus one, which corresponds to a letter in the alphabet. The function prints the concatenated answer strings for all test cases.

