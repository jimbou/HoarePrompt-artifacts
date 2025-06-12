#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 100), then t sets of inputs. Each set of inputs contains an integer n (2 <= n <= 10) and n strings of length n consisting of characters '0' or '1'.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: `t` is an integer between 1 and 100 (inclusive), `i` is `t`, `n` is an integer between 2 and 10 (inclusive), `j` is `n-1`, `stdin` is empty, `a` is either 'Triangle' or 0, `b` is either 'Square' or an empty string.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts t sets of inputs, where each set contains an integer n and n strings of length n consisting of characters '0' or '1'. The function then checks each string for the presence of '1' characters and prints 'Triangle' if exactly one '1' is found, 'Square' if more than one '1' is found, or nothing if no '1' is found. After processing all inputs, the function leaves the program in a state where stdin is empty and the output is printed to the console.

