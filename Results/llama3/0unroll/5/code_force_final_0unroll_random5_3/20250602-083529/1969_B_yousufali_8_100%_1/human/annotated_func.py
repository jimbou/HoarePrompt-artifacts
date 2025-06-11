#State of the program right berfore the function call: s is a binary string (a string consisting of only 0-s and/or 1-s) of length at least 2.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: The final state of the variables after the loop has finished executing is: s is unchanged, n is the total number of '1's in the string s, and ans is the total number of '0's in the string s that are preceded by at least one '1'.
    print(ans)
    #This is printed: the total number of '0's in the string s that are preceded by at least one '1'

#Overall this is what the function does:The function takes a binary string as input and returns the total number of '0's in the string that are preceded by at least one '1'. The input string remains unchanged.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings (strings consisting of only 0-s and/or 1-s) with lengths between 2 and 2 * 10^5.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The output state is the same as the initial state, with the variable `t` being the only one affected. After the loop finishes executing, `t` will be 0, and the stdin will still contain the same binary strings as before. The lengths of the binary strings will remain unchanged, between 2 and 2 * 10^5.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t binary strings, and then executes a loop t times, calling a function func_1() in each iteration. After the loop finishes, the function does not return any value or modify the input binary strings, leaving the standard input unchanged. The only side effect is that the variable t is decremented to 0.

