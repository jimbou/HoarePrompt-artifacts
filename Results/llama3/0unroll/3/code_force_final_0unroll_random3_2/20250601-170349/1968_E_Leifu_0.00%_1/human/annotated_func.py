#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 50) and then t integers (2 ≤ n ≤ 10^3).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: The loop will print a series of numbers to the console, with each iteration of the outer loop printing a different set of numbers. The first two lines of each iteration will always be "1 1" and "1 2". If the input number `n` is 3, the third line will be "2 3", otherwise it will be "2 4". For `n` greater than 3, the loop will print additional lines with the number `j` repeated twice, where `j` ranges from 4 to `n` inclusive. The value of `t` will be unchanged, and the input numbers will be consumed from stdin.

#Overall this is what the function does:Prints a series of numbers to the console, with each set of numbers corresponding to a different input number `n`. For each `n`, it prints "1 1" and "1 2", followed by either "2 3" if `n` is 3, or "2 4" and additional lines with repeated numbers from 4 to `n` if `n` is greater than 3. The function consumes input numbers from stdin and does not return any value.

