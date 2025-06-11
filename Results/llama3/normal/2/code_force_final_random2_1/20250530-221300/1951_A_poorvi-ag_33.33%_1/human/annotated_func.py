#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 50) and then a binary string of size n.
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('1') == 2 and '11' in arr:
            results.append('no')
        
        if arr.count('1') % 2 == 0:
            if arr.count('1') == 2 and '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('no')
        
    #State: t is an integer greater than or equal to 0, i is t, n is an integer, arr is a string, results is a list containing the string 'yes' or 'no' t times. If arr contains an even number of '1's, then 'yes' is added to results if arr does not contain exactly two '1's and '11' as a substring. Otherwise, 'no' is added to results. If arr contains an odd number of '1's, then 'no' is added to results once if arr does not contain exactly two '1's and '11' as a substring. Otherwise, 'no' is added to results twice.
    for r in results:
        print(r)
        
    #State: `t` is an integer greater than or equal to 0, `i` is `t`, `n` is an integer, `arr` is a string, `results` is a list containing the string 'yes' or 'no' `t` times, and all elements in the list which are 'yes' or 'no' have been printed

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a binary string of size n. It then checks each binary string to determine if it meets certain conditions. If the string contains an even number of '1's and does not contain exactly two '1's and '11' as a substring, it appends 'yes' to the results list. Otherwise, it appends 'no' to the results list. The function repeats this process for all test cases and finally prints all the results.

