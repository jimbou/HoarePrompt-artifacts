#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are non-negative integers of the same length, consisting only of digits from 1 to 9.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        mid = len(a) // 2
        
        i = 0
        
        while i < mid:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        while i < len(a):
            new[i] = min(a[i], b[i])
            new2[i] = max(a[i], b[i])
            i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: `stdin` is empty, `new` and `new2` are not defined, `a` and `b` are not defined, `mid` is not defined, `i` is not defined, `_` is `t`, and `t` pairs of strings are printed, each pair consisting of the maximum and minimum of the corresponding input pairs.

#Overall this is what the function does:This function reads input from stdin, processes it in pairs of integers, and prints out the maximum and minimum of each pair. It takes no parameters and returns no value, instead printing the results directly. The function's purpose is to compare pairs of integers and output the maximum and minimum values for each pair. After execution, the stdin is empty, and the function's variables are no longer defined. The function performs the action of comparing and printing the maximum and minimum of input pairs.

