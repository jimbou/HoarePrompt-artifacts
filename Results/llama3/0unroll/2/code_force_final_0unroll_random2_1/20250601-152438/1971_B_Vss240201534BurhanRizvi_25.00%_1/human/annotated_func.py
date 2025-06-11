#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings s of length at most 10 consisting of lowercase English letters.
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The output contains t lines, each containing either 'No' or 'Yes' followed by a random permutation of the input string s. If the randomly generated string s2 is the same as the original string s, the output is 'No'. Otherwise, the output is 'Yes' followed by the randomly generated string s2.

#Overall this is what the function does:This function generates and prints random permutations of input strings. It reads an integer t from standard input, followed by t strings. For each string, it generates a random permutation and checks if it is different from the original string. If it is, the function prints 'Yes' followed by the permuted string. If the permuted string is the same as the original, it prints 'No'. The function repeats this process t times, printing the results for each input string.

