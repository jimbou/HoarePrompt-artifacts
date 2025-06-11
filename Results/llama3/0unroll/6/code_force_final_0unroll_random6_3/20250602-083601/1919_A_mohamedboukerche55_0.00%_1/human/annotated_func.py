#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two space-separated integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: stdin is empty, and the variables a and b hold the values of the last pair of integers from the input.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: *stdin is empty, and the variables a and b hold the values of the last pair of integers from the input. If the sum of a and b is even, 'bob' is being printed. If the sum of a and b is odd, 'alice' is being printed.

#Overall this is what the function does:Reads a series of pairs of integers from standard input, and for each pair, prints 'bob' if the sum of the pair is even, and 'alice' if the sum is odd.

