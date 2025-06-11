#State of the program right berfore the function call: path is a list of characters where each character is either '@' or '*'.
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns the number 0.
    #State: *`path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, and `n` is larger than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: *`path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, `n` is larger than 0, `dp` is a list of `n` numbers where the first number is -float('inf') and the rest are zeros, the first character of `path` is '*', and the current value of the first character of `path` is '*'
    #State: *`path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, `n` is larger than 0. If the first character of `path` is '@', then `dp` is a list of `n` integers where `dp[0]` is 1 and the rest are 0. If the first character of `path` is '*', then `dp` is a list of `n` numbers where the first number is -float('inf') and the rest are zeros.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: *`path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, `n` is larger than 1. If the first character of `path` is '@', then the current value of `dp` is a list of `n` integers where `dp[0]` is 1 and the rest are 0. If the first character of `path` is '*', then the current value of `dp` is a list of `n` numbers where the first number is -float('inf') and the rest are zeros. If the second character of `path` is '*', then `dp[1]` is -float('inf'). If the second character of `path` is '@', then `dp[1]` is 1 if the first character of `path` is '@' else `dp[1]` is 1. If the second character of `path` is not '*' and the first character of `path` is '*', then `dp[1]` is 0.
    #State: *`path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, `n` is larger than 0. If `n` is 1, then the value of `dp` is determined by the first character of `path`. If the first character of `path` is '@', then `dp` is a list of `n` integers where `dp[0]` is 1 and the rest are 0. If the first character of `path` is '*', then `dp` is a list of `n` numbers where the first number is -float('inf') and the rest are zeros. If `n` is larger than 1, then the value of `dp` is determined by the first two characters of `path`. If the second character of `path` is '*', then `dp[1]` is -float('inf'). If the second character of `path` is '@', then `dp[1]` is 1 if the first character of `path` is '@' else `dp[1]` is 1. If the second character of `path` is not '*' and the first character of `path` is '*', then `dp[1]` is 0.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `path` is a list of characters where each character is either '@' or '*', `n` is the number of characters in `path`, `n` is larger than 0, `i` is `n`, `dp` is a list of `n` numbers where the value of each number is determined by the corresponding character in `path`. If the character at index `i` of `path` is '*', the number at index `i` in `dp` is negative infinity. Otherwise, the character at index `i` of `path` is '@', and the value of `dp[i]` is the maximum of `dp[i - 1]` and `dp[i - 2]` plus 1.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value in the list `dp` that is greater than negative infinity, which represents the maximum value that can be obtained by traversing the path from the beginning to the end, where '*' represents an obstacle and '@' represents a valid path, and the value at each position is the maximum of the values at the previous two positions plus 1, or negative infinity if the character at that position is '*'.

#Overall this is what the function does:This function calculates the maximum value that can be obtained by traversing a path from the beginning to the end, where '*' represents an obstacle and '@' represents a valid path. The function takes a list of characters as input, where each character is either '@' or '*', and returns the maximum value that can be obtained by traversing the path. If the input list is empty, the function returns 0. Otherwise, the function iterates through the list, assigning a value to each position based on the maximum of the values at the previous two positions plus 1, or negative infinity if the character at that position is '*'. The function then returns the maximum value in the list that is greater than negative infinity.

#State of the program right berfore the function call: data is a list of strings where data[0] is a positive integer, and for every i > 0, data[i] is either a positive integer or a string that can be converted to a list of positive integers separated by spaces.
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        path = data[index]
        
        index += 1
        
        results.append(func_1(path))
        
    #State: data is an empty list, t is 0, index is 2*t+1, results is a list containing t elements which are the return values of func_1(path) for t different paths, stdin is empty
    for result in results:
        print(result)
        
    #State: data is an empty list, t is at least 1, index is 2*t+1, results is an empty list, stdin is empty, and all elements of the results list have been printed.

#Overall this is what the function does:Reads input from standard input, processes it, and prints the results.

