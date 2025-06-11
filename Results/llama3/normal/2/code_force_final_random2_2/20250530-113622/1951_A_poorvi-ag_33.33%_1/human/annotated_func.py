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
        
    #State: t is equal to 0, i is equal to t, n is an integer between 1 and 50, arr is a binary string of size n, stdin is empty. If arr contains exactly two '1's and '11' is a substring of arr, results is a list containing t strings 'no'. If arr does not contain exactly two '1's or '11' is not a substring of arr, and the count of '1's in arr is even, results is a list containing t strings 'yes' and 'no'. If arr does not contain exactly two '1's or '11' is not a substring of arr, and the count of '1's in arr is odd, results is a list containing t strings 'no'.
    for r in results:
        print(r)
        
    #State: t is 0, i is 0, n is an integer between 1 and 50, arr is a binary string of size n that does not contain exactly two '1's or '11' is not a substring of arr, and the count of '1's in arr is even, results is a list containing t strings 'yes' and 'no', r is the last element in the list results, stdin is empty, and the last element in the list results which is r is being printed, and 'yes' or 'no' is being printed, and the value of r which is either 'yes' or 'no' is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a binary string of size n. It then checks each binary string to determine if it meets certain conditions. If the string contains exactly two '1's and '11' is a substring, it appends 'no' to the results list. If the string does not contain exactly two '1's or '11' is not a substring, and the count of '1's is even, it appends 'yes' to the results list. If the string does not contain exactly two '1's or '11' is not a substring, and the count of '1's is odd, it appends 'no' to the results list. Finally, it prints each result in the results list.

