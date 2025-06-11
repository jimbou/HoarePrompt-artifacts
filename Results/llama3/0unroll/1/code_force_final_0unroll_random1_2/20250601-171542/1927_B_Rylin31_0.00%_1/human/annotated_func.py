#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of an integer n, followed by n integers a_1, a_2, ..., a_n.
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
        
    #State: The output state will be a series of strings, each representing the modified array for each test case. The modification involves replacing each number in the array with a letter from the alphabet, where the letter is determined by the count of the number in the reversed array, minus one. The resulting strings are then printed out, one for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then modifies each test case by replacing each number with a letter from the alphabet, determined by the count of the number in the reversed array minus one. The modified arrays are then printed out as strings, one for each test case.

