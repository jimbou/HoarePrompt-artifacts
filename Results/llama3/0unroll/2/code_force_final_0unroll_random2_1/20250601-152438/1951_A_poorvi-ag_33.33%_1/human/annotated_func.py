#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer t (1 <= t <= 1000) representing the number of test cases. The second line contains an integer n (1 <= n <= 50) representing the number of lamps, followed by a binary string s of size n representing the final desired configuration.
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
        
    #State: Output State: The value of variable t is 0, results is a list containing 'yes' or 'no' for each test case, stdin is empty.
    for r in results:
        print(r)
        
    #State: Output State: The value of variable t is 0, results is a list containing 'yes' or 'no' for each test case, stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer representing the number of lamps and a binary string representing the desired configuration. It then determines whether the desired configuration can be achieved and outputs 'yes' or 'no' for each test case, depending on whether the number of '1's in the binary string is even and does not contain consecutive '1's. The function processes all test cases and prints the results, leaving the input stream empty.

