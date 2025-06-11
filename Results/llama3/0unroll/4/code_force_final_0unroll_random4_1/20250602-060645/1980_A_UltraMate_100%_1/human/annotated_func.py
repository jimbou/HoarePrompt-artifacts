#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two integers n and m (1 <= n <= 50, 1 <= m <= 5) followed by a string a of n characters from 'A' to 'G'.
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: The output state will contain `t` number of integers, each representing the total number of characters that need to be added to the string `a` to make all characters appear at least `m` times. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the total number of characters needed to be added to each test case string to make all characters appear at least a certain number of times. It takes no parameters and returns no value, instead printing the results directly. The function modifies the input string by counting the occurrences of each character and calculating the difference between the desired count and the actual count, then prints the total number of characters needed to be added. The function does not modify the input variables, only using them to calculate and print the results.

